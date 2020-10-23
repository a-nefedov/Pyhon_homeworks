"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу..
"""


def my_func(args):
    """
    суммирует все числа из входящего списка
    :param args: список из чисел
    :return: сумму чисел из списка
    """
    sum_args = 0
    tmp = 0
    while tmp < len(args):
        arg = (args[tmp])
        sum_args += arg
        tmp += 1
    return sum_args


args = []
c = 0
while c != 1:
    for arg in input('Введите числа через пробел\nДля выхода, введите q\n>>>').split(sep=' '):
        if arg != 'q':
            try:
                args.append(int(arg))
            except ValueError:
                print('Введено не число')
        else:
            c = 1
            break
    print(my_func(args))
