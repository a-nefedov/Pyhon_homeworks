"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("tmp_file.txt", "w") as file:
    numbers = input('Введите числа через пробел')
    file.write(numbers)
    try: print(sum(int(i) for i in numbers.split(sep=' ')))
    except ValueError:
        print('Введены не числа')
