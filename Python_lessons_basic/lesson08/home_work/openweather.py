
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""


import sqlite3
import requests
import gzip
import io
import json
import os
import sys
from datetime import datetime


# возвращает id приложения для выполнения авторизованных запросов
def get_app_id():
    file_name = 'app.id'
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()


# функция-декоратор обработки ошибок базы данных
def exeption_handling_db(func):
    def call_func(obj, *args):
        try:
            return func(obj, *args)
        except sqlite3.DatabaseError as err:
            print("Error: ", err)

    return call_func


class WeatherDatabase:
    def __init__(self, name_db):
        self.name_db = name_db
        self.conn = sqlite3.connect(self.name_db)
        self.cur = self.conn.cursor()

    def close_connect(self):
        self.conn.close()
        print("Соединение с SQLite закрыто")

    @exeption_handling_db
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS weather(
               cityid INTEGER PRIMARY KEY,
               city VARCHAR(255),
               date DATE,
               temperature INTEGER,
               weatherid INTEGER
           );""")
        self.conn.commit()

    @exeption_handling_db
    def add_row(self, cityid, city, date, temperature, weatherid):
        row = self.cur.execute('SELECT * FROM weather WHERE cityid=? AND date=?', (cityid, date))
        if row.fetchone() is None:
            self.cur.execute("""INSERT INTO weather VALUES(?, ?, ?, ?, ?);""",
                             (cityid, city, date, temperature, weatherid))
        else:
            self.update_row(cityid, city, date, temperature, weatherid)

        self.conn.commit()

    @exeption_handling_db
    def add_rows(self, rows):
        self.cur.executemany("INSERT INTO weather VALUES(?, ?, ?, ?, ?);", rows)
        self.conn.commit()

    @exeption_handling_db
    def get_rows_all(self):
        self.cur.execute("SELECT * FROM weather;")
        results = self.cur.fetchall()
        return results

    @exeption_handling_db
    def get_rows_filter_city(self, city):
        self.cur.execute("SELECT * FROM weather WHERE city=?;", (city,))
        results = self.cur.fetchall()
        return results

    @exeption_handling_db
    def update_row(self, cityid, city, date, temperature, weatherid):
        self.cur.execute("""UPDATE weather SET city = ?, temperature = ? WHERE cityid=? AND date=?;""", (city, temperature, cityid, date))
        self.conn.commit()

    @exeption_handling_db
    def del_row(self, cityid):
        self.cur.execute("DELETE FROM weather WHERE cityid = ?;", (cityid,))
        self.conn.commit()


# возвращает список кодов стран
def get_country_list(cities_list):
    countries = []
    for obj in cities_list:
        countries.append(obj['country'])
    return sorted(set(countries))


# возвращает список объектов городов
def get_city_list(f_name):
    if not os.path.exists(f_name):
        ref = requests.get('http://bulk.openweathermap.org/sample/city.list.json.gz')
        file = ref.content
        with gzip.open(io.BytesIO(file), 'rb') as data:
            with io.TextIOWrapper(data, encoding='utf-8') as decoder:
                cities_str = decoder.read()

        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(cities_str)

    with open(f_name, 'r', encoding='utf-8') as f:
        return json.load(f)


# возвращает список объектов городов найденных по первым буквам
def search_cities(cities_list, city):
    lst = []
    for obj in cities_list:
        # if obj['name'].startswith(city.title()):
        #     lst.append(obj)
        #     continue
        if obj['country'] == city.upper():
            lst.append(obj)

    return lst


# возвращает данные о текущей погоде в городе id_city
def get_weather(id_city):
    app_id = get_app_id()
    url = f'http://api.openweathermap.org/data/2.5/weather?id={id_city}&units=metric&appid={app_id}'
    res = requests.get(url)
    return res.json()


# получить погоду списка городов
def get_weathers(ids):
    result = []
    length = 20
    app_id = get_app_id()
    ids = [str(i) for i in ids]
    for i in range(0, len(ids), length):
        ids_str = ",".join(ids[i:i + length])
        url = f'http://api.openweathermap.org/data/2.5/group?id={ids_str}&units=metric&appid={app_id}'
        res = requests.get(url)
        result.extend(res.json()['list'])
        print("", end='\r')
        print(f'Выполнено {i} из {len(ids)} запросов.', end='')

    print('')
    return result


# вывод сгруппированного списка кодов стран
def display_countries(countries_list):
    prev = None
    for country in countries_list:
        if not country: continue
        if prev and prev[0] != country[0]:
            # пеенос строки для печати сновой строки
            print()
        print(country, end=', ')
        prev = country

    print()


# сохранение данных погоды
def save_weathers_to_db(db, weathers):
    print('Сохранение полученных данных в БД')
    for ind, weather in enumerate(weathers):
        cityid = weather['id']
        city = weather['name']
        date = datetime.fromtimestamp(int(weather['dt'])).date()
        temperature = weather['main']['temp']
        weatherid = weather['weather'][0]['id']

        db.add_row(cityid, city, date, temperature, weatherid)
        print(end='\r')
        print(f'Сохранено {ind} из {len(weathers)} записей', end='')

    print('')


def main():
    # список городов
    cities_list = get_city_list('data/city_list.json')
    # инициализация объета базы данных
    db = WeatherDatabase('weather.db')
    # создание таблицы в БД
    db.create_table()

    # список кодов стран
    countries = get_country_list(cities_list)
    print('Список кодов стран: ')
    display_countries(countries)

    while True:
        command = input('Введите код страны из списка выше для получения погодных данных (q - выход): ')
        if command == 'q':
            ws = db.get_rows_all()
            print(ws)
            print(len(ws))
            # закрытие подключения к БД
            db.close_connect()
            print('Программа закрыта')
            return

        # поиск городов для получения их погоды
        cities_search_list = search_cities(cities_list, command)
        cities_search_list = [obj['id'] for obj in cities_search_list]
        if not cities_search_list:
            print('Данный город отсутствует в базе данных')
            continue

        # получение данных погоды списка городов
        weathers = get_weathers(cities_search_list)

        # сохранение погоды в БД
        save_weathers_to_db(db, weathers)


if __name__ == '__main__':
    main()

