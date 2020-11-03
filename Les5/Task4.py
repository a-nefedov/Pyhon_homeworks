"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл
"""
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
my_file = open("tmpfile.txt", "w")
my_file.close()
with open("FileTask4.txt", "r") as file:
    for line in file.readlines():
        tmp_line = line.split(sep=' - ')
        with open("tmpfile.txt", "a", encoding="UTF-8") as tmp:
            tmp.write(f'{my_dict.get(tmp_line[0])} - {tmp_line[1]}')
