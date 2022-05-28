# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

n = 9
dir_name_template = 'dir_{}'


def create_dir(path):
    os.mkdir(path)
    if os.path.isdir(path):
        return True
    return False


def remove_dir(path):
    try:
        os.rmdir(path)
        if not os.path.isdir(path):
            return True
    except Exception:
        pass
    finally:
        return False


def create_dirs(path, count):
    for i in range(count):
        dir_name = os.path.join(path, dir_name_template.format(i + 1))
        os.mkdir(dir_name)


def remove_dirs(path, count):
    for i in range(count):
        dir_name = os.path.join(path, dir_name_template.format(i + 1))
        os.rmdir(dir_name)


# # create_dirs(os.getcwd(), 9)
# remove_dirs(os.getcwd(), 9)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#
# import os
#
#
# def show_folders_dir(path):
#     print(os.listdir(path))
#
#
# show_folders_dir(os.getcwd())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import copy_import_file

