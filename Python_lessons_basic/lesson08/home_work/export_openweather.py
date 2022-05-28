
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.
"""


import csv
import json
import argparse
import sys
import sqlite3
from openweather import WeatherDatabase


icon_dict = {
    '01d': [800],
    '02d': [801],
    '03d': [802],
    '04d': [803, 804],
    '09d': [300, 301, 302, 310, 311, 312, 313, 314, 321, 520, 521, 522, 531],
    '10d': [500, 501, 502, 503, 504],
    '11d': [200, 201, 202, 210, 211, 212, 221, 230, 231, 232],
    '13d': [511, 600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622],
    '50d': [701, 711, 721, 731, 741, 751, 761, 762, 771, 781],
}
icons = {code: key for key, values_list in icon_dict.items() for code in values_list}


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv')
    parser.add_argument('--json')
    parser.add_argument('--html')
    parser.add_argument('city', nargs='?')
    return parser


def write_to_csv(f_name, weathers):
    with open(f_name, 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f, lineterminator='\r')
        f_csv.writerow(['id_города', 'Город ', 'Дата', 'Температура', 'id_погоды'])
        f_csv.writerows(weathers)


def write_to_json(f_name, weathers):
    with open(f_name, 'w', encoding='utf-8') as f:
        json.dump(weathers, f)


def write_to_html(f_name, weathers):
    with open(f_name, 'w', encoding='utf-8') as f:
        content = ''
        for weather in weathers:
            key = weather[4]
            icons[key]
            content += f"""
                <tr>
                    <td>{weather[0]}</td>
                    <td>{weather[1]}</td>
                    <td>{weather[2]}</td>
                    <td>{weather[3]}</td>
                    <td>
                        <img src="http://openweathermap.org/img/wn/{icons[key]}.png">
                    </td>
                </tr>
            """
        contentHTML = f"""
            <!DOCTYPE HTML>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Данные погоды</title>
                </head>
                <body>
                    <table border="1">
                        <caption>Данные погоды</caption>
                        <tr>
                            <th>id_города</th>
                            <th>Город</th>
                            <th>Дата</th>
                            <th>Температура</th>
                            <th>id_погоды</th>
                        </tr>
                        {content}
                    </table>
                </body>
            </html>
        """
        f.write(contentHTML)


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    # инициализация объета базы данных
    db = WeatherDatabase('weather.db')
    if namespace.city:
        weathers = db.get_rows_filter_city(namespace.city)
    else:
        weathers = db.get_rows_all()

    # write_to_csv(namespace.csv, weathers)
    # write_to_json(namespace.json, weathers)
    write_to_html(namespace.html, weathers)


