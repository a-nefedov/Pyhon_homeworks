"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce
import functions as f


def my_func(a, b):
    return a * b


my_list = []
[my_list.append(el) for el in f.my_range(100, 1001) if el % 2 == 0]

print(reduce(my_func, my_list))
