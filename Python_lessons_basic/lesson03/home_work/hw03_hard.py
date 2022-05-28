# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# def summation_fractions(a, b, operator):
#     a_list = parsing_fractions(a)
#     b_list = parsing_fractions(b)
#     print(a_list)
#     print(b_list)
#
#     common_denominator = a_list[1] * b_list[1]
#     if operator == '+':
#         numerator = a_list[0] * b_list[1] + a_list[1] * b_list[0]
#     else:
#         numerator = a_list[0] * b_list[1] - a_list[1] * b_list[0]
#
#     # при отсутствии дробной части
#     if not (numerator % common_denominator):
#         return f'{numerator // common_denominator}'
#
#     # при наличии целой и дробной части
#     if abs(numerator) >= common_denominator:
#         integer = numerator // common_denominator
#         numerator -= integer * common_denominator
#         return f'{integer} {abs(numerator)}/{common_denominator}'
#
#     #  при наличии только дробной части
#     return f'{numerator}/{common_denominator}'
#
#
# def parsing_fractions(fraction):
#     sign = '-' if fraction.startswith('-') else '+'     # знак дроби
#     fraction = fraction.replace('-', '')                # удаление знака
#     integer = None          # целая часть
#     numerator = None        # числитель
#     denominator = None      # знаменатель
#
#     # при наличии пробельного разделителя
#     if ' ' in fraction:
#         integer, fraction = fraction.split()            # деление строки на целую и дробную часть
#
#     # при наличии знака деления
#     if '/' in fraction:
#         numerator, denominator = fraction.split('/')
#
#     # если дробная часть отсутствует
#     if integer is None and numerator is None and denominator is None:
#         integer = fraction
#
#     # при наличии целой части избавление от нее
#     if integer is not None and numerator is not None and denominator is not None:
#         numerator = int(integer) * int(denominator) + int(numerator)
#
#     # при наличии целой части и отсутствии дробной части
#     if integer is not None and numerator is None and denominator is None:
#         numerator = int(integer)
#         denominator = 1
#
#     if sign == '-':
#         numerator = int(f'-{numerator}')
#
#     return int(numerator), int(denominator)
#
#
# def input_equation():
#     # equation = input('Введите уравнение: ')
#     equation = "-2/3 - -2"
#     fraction_1 = None
#     fraction_2 = None
#     operator = None
#     arr_add = equation.split(" + ")
#     arr_dif = equation.split(" - ")
#     if len(arr_add) > 1:
#         operator = '+'
#         fraction_1, fraction_2 = arr_add
#     if len(arr_dif) > 1:
#         operator = '-'
#         fraction_1, fraction_2 = arr_dif
#
#     # print(parsing_fractions(fraction_1))
#     res = summation_fractions(fraction_1, fraction_2, operator)
#     print(res)
#
# input_equation()


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# import os
# import pprint
#
#
# def salary_calculation(file_workers, file_hours_of):
#     path_workers = os.path.join('data', file_workers)
#     path_hours_of = os.path.join('data', file_hours_of)
#
#     worker_data = []
#     with open(path_workers, 'r', encoding='utf-8') as f:
#         f.readline()        # пропуск строки заголовка таблицы (первая строка)
#         for line in f:
#             lst = line.split()
#             worker_data.append({
#                 "name": lst[0],
#                 "lastname": lst[1],
#                 "revenue": int(lst[2]),
#                 "norm_hours": int(lst[4]),
#             })
#
#     hoours_data = []
#     with open(path_hours_of, 'r', encoding='utf-8') as f:
#         f.readline()
#         for line in f:
#             row = line.split()
#             hoours_data.append(row)
#
#     summary_data = []
#     for worker in worker_data:
#         for hours_worker in hoours_data:
#             if hours_worker[0] == worker['name'] and hours_worker[1] == worker['lastname']:
#                 summary_data.append({
#                     'name': worker['name'],
#                     'lastname': worker['lastname'],
#                     'many': int(hours_worker[2]) * worker['revenue'] / worker['norm_hours'],
#                 })
#
#     pprint.pprint(summary_data)


# salary_calculation('workers', 'hours_of')

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
# print(list(range(ord('А'), ord('Я')+1)))

import os


def grouping_data(file_name):
    path = os.path.join('data', file_name)
    data = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            char = line[0].capitalize()
            if data.get(char):
                data[char].append(line)
            else:
                data[char] = [line]

    for key, values in data.items():
        path = os.path.join('data', f'fruit_{key}')
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(values)


grouping_data('fruits.txt')


