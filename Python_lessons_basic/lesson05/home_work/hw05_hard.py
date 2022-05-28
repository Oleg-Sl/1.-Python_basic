# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil
import re


print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))


def copy():
    if not name:
        print('Необходимо указать имя файла вторым параметром')
        return

    src = os.path.join(os.getcwd(), name)

    i = 1
    while True:
        dst = os.path.join(os.getcwd(), re.sub(r'()(?=\.\w+)', f'({i})', name))
        if not os.path.isfile(dst):
            break
        i += 1

    try:
        shutil.copy(src, dst)
    except FileNotFoundError:
        print('указанный файл доя копирования не существует')


def remove():
    if not name:
        print('Необходимо указать имя удаляемого файла вторым параметром')
        return

    src = os.path.join(os.getcwd(), name)

    try:
        os.remove(src)
    except FileNotFoundError:
        print('Не удается найти указанный файл для удаления')


def goto_dir():
    if not name:
        print('Необходимо указать полный или относительный путь директории для перехода')
        return
    try:
        if re.match('/', name) or re.match('\w:', name):
            path = os.path.abspath(f'{name}')
        else:
            path = os.path.join(os.getcwd(), name)
        os.chdir(fr'{path}')
        print(f'Успешно перешли в директорию {os.getcwd()}')
    except FileNotFoundError:
        pass


def listdir():
    print(f'Путь текущей директории: {os.getcwd()}')


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy,
    "rm": remove,
    "cd": goto_dir,
    "ls": listdir
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")



