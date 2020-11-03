"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open('FileTask2.txt', "r") as file:
    count_line = 0
    for line in file.readlines():
        count_line += 1
        count_word = 0
        for word in line.split(sep=' '):
            count_word += 1
        print(f'Количество слов в {count_line} строке равно {count_word}')
    print(f'Количество строк в файле равно {count_line}')
