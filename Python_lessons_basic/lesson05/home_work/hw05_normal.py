# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import hw05_easy


def get_dir_name():
    return input('Введите название папки: ')


if __name__ == '__main__':
    while True:
        command = input('Введите номер команды (меню команд "9"): ')
        # Выход
        if command == '0':
            break

        # Перейти в папку
        if command == '1':
            current_dir = os.getcwd()       # текущая директория
            dir_name = get_dir_name()       # имя директории в которую перейти
            children_patch = os.path.join(current_dir, dir_name)    # путь директории, к которой перейти
            if os.path.isdir(children_patch):
                os.chdir(children_patch)
            if os.path.isdir(children_patch) and os.path.samefile(children_patch, os.getcwd()):
                print(f'Успешно перешел в директорию: {children_patch}')
            else:
                print(f'Невозможно перейти в директорию: {children_patch}')
        # Просмотреть содержимое текущей папки
        if command == '2':
            print('Содердимое текущей папки:')
            for f in os.listdir():
                print('    ', f)
        # Удалить папку
        if command == '3':
            dir_name = get_dir_name()
            if hw05_easy.remove_dir(dir_name):
                print(f'Успешно удалена директория: {parent_dir}')
            else:
                print(f'Невозможно удалить директорию: {parent_dir}')
        # Создать папку
        if command == '4':
            dir_name = get_dir_name()
            if hw05_easy.create_dir(dir_name):
                print(f'Успешно создана директория: {parent_dir}')
            else:
                print(f'Невозможно создать директорию: {parent_dir}')
        # Перейти в родительскую папку
        if command == '5':
            current_dir = os.getcwd()
            parent_dir, _ = os.path.split(current_dir)
            os.chdir(parent_dir)
            if os.path.isdir(parent_dir) and os.path.samefile(parent_dir, os.getcwd()):
                print(f'Успешно перешел в директорию: {parent_dir}')
            else:
                print(f'Невозможно перейти в директорию: {parent_dir}')

        if command == '9':
            print("\
                1. Перейти в папку\n\
                2. Просмотреть содержимое текущей папки\n\
                3. Удалить папку\n\
                4. Создать папку\n\
                5. Перейти в родительскую папку\n\
                9. Меню команд\n\
                0. Выход\n\
            ")
