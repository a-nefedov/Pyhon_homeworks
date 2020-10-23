"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(a, b, c):
    """Возвращает сумму двух наибольших из трёх введённых чисел"""
    if a > b:
        return a + c
    elif a > c:
        return a + b
    else:
        return b + c

try: value1, value2, value3 = float(input('\n>>>')), float(input('\n>>>')), float(input('\n>>>'))
except ValueError:
    print('Введены не числа')
print(my_func(value1, value2, value3))
