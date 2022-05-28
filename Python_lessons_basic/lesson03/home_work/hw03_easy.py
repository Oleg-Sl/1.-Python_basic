# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


# def my_round(number, ndigits=None):
#     if ndigits is not None:
#         multiplier = 10 ** ndigits          # множитель
#     else:
#         multiplier = 1                      # множитель
#
#     number_mult = number * multiplier       # переданное число умноженное на множитель
#     if number_mult * 10 % 10 > 5:           # еслли число следующее за требуемым кол-вом знаков после "," >= 5
#         number_mult += 1
#
#     number_round = int(number_mult) / multiplier  # отбрасывание лишнх знаков после запятой и приведение к исходному виду
#     return int(number_round) if ndigits is None else number_round
#
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))
# print(my_round(0.501))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# def lucky_ticket(ticket_number):
#     length = 6
#     assert len(str(ticket_number)) == length, f"Длина номера билета должна быть равна {length}"
#     left = 10 ** (length - 1)
#     right = 10
#     diff = 0
#
#     while True:
#         if left < right:
#             break
#         diff += ticket_number % (left * 10) // left
#         diff -= ticket_number // (right / 10) % 10
#
#         left /= 10
#         right *= 10
#
#     if diff:
#         return 'Билет не счастливый('
#     return 'Билет счастливый)'

def lucky_ticket(ticket_number):
    length = 6
    number_str = str(ticket_number)
    assert len(number_str) == length, f"Длина номера билета должна быть равна {length}"
    diff = 0

    for i in range(length // 2):
        diff += int(number_str[i])
        diff -= int(number_str[-i - 1])

    if diff:
        return 'Билет не счастливый('
    else:
        return 'Билет счастливый)'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
