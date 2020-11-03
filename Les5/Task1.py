"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("some_file.txt", "w") as some_file:
    while True:
        some_string=input('Введите строку. Для окончания ввода, введите q')
        if some_string == 'q':
            break
        else:
            some_file.write(f'{some_string}\n')
