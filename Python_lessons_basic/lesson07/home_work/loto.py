#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import os


class Card:
    def __init__(self, values):
        self.card = values

    def is_number_in_card(self, number):
        numbers = [cell for row in self.card for cell in row if cell == number]
        if number in numbers:
            return True

    def cross_out_number(self, number):
        for i, row in enumerate(self.card):
            for j, cell in enumerate(row):
                if cell == number:
                    self.card[i][j] = '-'

    def is_win_card(self):
        remaining_numbers = [isinstance(cell, int) for row in self.card for cell in row if cell]
        # print(f'{remaining_numbers=}')
        if not remaining_numbers:
            return True

    def __str__(self):
        s = ''
        for row in self.card:
            for el in row:
                cell = el if el else ""
                s += f'{cell:2} '
            s += '\n'
        return s


def generation_card():
    numbers = []
    while True:
        if len(numbers) > 15:
            break
        i = random.randint(1, 90)
        if i not in numbers:
            numbers.append(i)
    card_data = [
        sorted(numbers[:5]),
        sorted(numbers[5:10]),
        sorted(numbers[-5:]),
    ]
    for row in card_data:
        for _ in range(4):
            row.insert(random.randint(0, len(card_data)), '')

    return card_data


def game():
    # объекты карточек
    user_card = Card(generation_card())
    computer_card = Card(generation_card())

    # список номеров бочонков
    numbers = [i for i in range(1, 91)]
    random.shuffle(numbers)

    for number in numbers:
        # Вывод текущего бочонка
        print(f'\033[1m\033[4mНомер бочонка: {number}\033[0m', end='\n\n')

        # Вывод карточек игрокоов
        print('\033[32m{:-^26}\033[0m'.format(' Ваша карточка '))
        print(f'\033[32m{user_card}\033[0m')
        print('\033[34m{:-^26}\033[0m'.format('Карточка компьютера'))
        print(f'\033[34m{computer_card}\033[0m')

        # выбор действия
        while True:
            command = input('Введите номер команды (1 - зачеркнуть, 2 - продолжить, 0 - выйти): ')
            if command == '0':
                print('Игра завершена')
                return
            elif command in ['1', '2']:
                break
            else:
                print('Введите правильную кмоманду')

        if command == '1':
            if user_card.is_number_in_card(number):
                # вычеркивание числа из карточки игрока
                user_card.cross_out_number(number)
            else:
                print('\033[31mВы проиграли')
                return

        if command == '2':
            if user_card.is_number_in_card(number):
                print('\033[31mВы проиграли')
                return

        # вычеркивание числа из карточки компьютера
        computer_card.cross_out_number(number)

        #
        if user_card.is_win_card() and computer_card.is_win_card():
            print('\033[31mНиччья')
            return

        if user_card.is_win_card():
            print('\033[31mПоздравляем, Вы выиграли!')
            return

        if computer_card.is_win_card():
            print('\033[31mК сожалению, Вы проиграли')
            return

        print('\n')


if __name__ == '__main__':
    game()





