"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль..
"""


def devide_func(a, b):
    """Делит первое число на второе"""
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


try:
    devidend, devider = float(input('Введите делимое\n>>>')), float(input('Введите делитель\n>>>'))
except ValueError:
    print('Введено не число :(')

print(devide_func(devidend, devider))