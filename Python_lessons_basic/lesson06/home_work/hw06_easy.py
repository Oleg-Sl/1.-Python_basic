from math import sqrt
from collections import namedtuple


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.points = (tuple(point_1), tuple(point_2), tuple(point_3),)
        # self.point_1 = tuple(point_1)

    def area(self):
        p = self.perimeter() / 2
        length_list = [self._length(self.points[ind - 1], self.points[ind]) for ind in range(len(self.points))]
        area = sqrt(p * (p - length_list[0]) * (p - length_list[1]) * (p - length_list[2]))
        return area

    def height(self):
        p = self.perimeter() / 2
        length_list = [self._length(self.points[ind - 1], self.points[ind]) for ind in range(len(self.points))]
        height_list = [2 * sqrt(p * (p - length_list[0]) * (p - length_list[1]) * (p - length_list[2])) / length for length in length_list]
        return max(height_list)

    def perimeter(self):
        p = 0
        for ind in range(len(self.points)):
            p += self._length(self.points[ind - 1], self.points[ind])

        return p

    @staticmethod
    def _length(p_1, p_2):
        return sqrt((p_2[0] - p_1[0]) ** 2 + (p_2[1] - p_1[1]) ** 2)


# t_1 = Triangle((1, 2), (5, 6), (8, 1))
# print(t_1.perimeter())
# print(t_1.height())
# print(t_1.area())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class IsoscelesTrapezoid:
    Point = namedtuple('Point', ['x', 'y'])

    def __init__(self, point_1, point_2, point_3, point_4):
        # self.points = (tuple(point_1), tuple(point_2), tuple(point_3), tuple(point_4),)
        self.points = (self.Point(*point_1), self.Point(*point_2), self.Point(*point_3), self.Point(*point_4))
        # self.point_1 = self.Point(*point_1)
        # self.point_2 = self.Point(*point_2)
        # self.point_3 = self.Point(*point_3)
        # self.point_4 = self.Point(*point_4)

    def lengths(self):
        return [self._length(self.points[ind - 1], self.points[ind]) for ind in range(len(self.points))]

    def perimeter(self):
        return sum(self.lengths())

    def area(self):
        lst = []
        for ind in range(len(self.points)):
            Parallel = namedtuple('Parallel', ['point_1', 'point_2', 'tg'])
            tg = (self.points[ind][1] - self.points[ind - 1][1]) / (self.points[ind][0] - self.points[ind - 1][0])
            lst.append(Parallel(self.points[ind - 1], self.points[ind], tg))
            print('*'*99)
            print('1 = ', self.points[ind])
            print('2 = ', self.points[ind - 1])
            print(f'{tg=}')

        for ind in range(len(lst) // 2):
            if lst[ind].tg == lst[ind + 2].tg:
                # print(lst[ind])
                # print(lst[ind + 2])
                # точки - 1 линия
                x1_1, y1_1 = lst[ind].point_1
                x1_2, y1_2 = lst[ind].point_2
                # точки - 2 линия
                x2_1, y2_1 = lst[ind + 2].point_1
                x2_2, y2_2 = lst[ind + 2].point_2
                # длины параллельных прямых
                a = self._length(lst[ind].point_1, lst[ind].point_2)
                b = self._length(lst[ind + 2].point_1, lst[ind + 2].point_2)

                # A = y1_1 - y1_2
                # B = -x1_1 + x1_2
                # C = x1_1 * y1_2 - x1_2 * y1_1
                #
                # d = abs(A * x2_1 + B * y2_1 + C) / sqrt(A ** 2 + B ** 2)
                # print(f'{A=}')
                # print(f'{B=}')
                # print(f'{d=}')
                print(f'{a=}')
                print(f'{b=}')
                # return (a + b) * d / 2

    @staticmethod
    def _length(p_1, p_2):
        # print(f'{p_1=}')
        # print(f'{p_2=}')
        return sqrt((p_2.x - p_1.x) ** 2 + (p_2.y - p_1.y) ** 2)


trap = IsoscelesTrapezoid((1, 1), (9, 1), (8, 5), (2, 5))
# print(trap.lengths())
# print(trap.perimeter())
print(trap.area())


