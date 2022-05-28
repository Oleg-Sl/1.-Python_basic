# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


# def fibonacci(n, m):
#     lst = [1, 1, ]
#     for i in range(2, m):
#         lst.append(lst[i - 2] + lst[i - 1])
#
#     return lst[n - 1:m + 1]
#
#
# print(fibonacci(7, 9))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
#     for ind in range(len(origin_list)):
#         min = origin_list[ind]
#         for i in range(ind + 1, len(origin_list)):
#             if origin_list[i] < min:
#                 min = origin_list[i]
#                 origin_list[ind], origin_list[i] = origin_list[i], origin_list[ind]
#
#     print(origin_list)
#
#
# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
# def my_filter(f, iterable):
#     lst = []
#     for el in iterable:
#         if f(el):
#            lst.append(el)
#     return lst
#
#
# res = my_filter(lambda el: True if el >=0 else False, [2, 10, -12, 2.5, 20, -11, 4, 4, 0])
# print(res)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def check_is_parallelogram(**kwargs):
    len_1 = (kwargs['x2'] - kwargs['x1']) ** 2 + (kwargs['y2'] - kwargs['y1']) ** 2
    len_2 = (kwargs['x3'] - kwargs['x2']) ** 2 + (kwargs['y3'] - kwargs['y2']) ** 2
    len_3 = (kwargs['x4'] - kwargs['x3']) ** 2 + (kwargs['y4'] - kwargs['y3']) ** 2
    len_4 = (kwargs['x1'] - kwargs['x4']) ** 2 + (kwargs['y1'] - kwargs['y4']) ** 2
    if len_1 == len_3 and len_2 == len_4:
        return True
    return False

is_parallelogram = check_is_parallelogram(**{
    'x1': 1,
    'y1': 1,
    'x2': 2,
    'y2': 3,
    'x3': 5,
    'y3': 3,
    'x4': 4,
    'y4': 1,
})
if is_parallelogram:
    print('Точки образуют параллелограм')
else:
    print('Точки не образуют параллелошрам')



