"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open("FileTask3.txt", "r") as file:
    sum_salary = 0
    employees = 0
    for line in file.readlines():
        tmp_line = line.split(sep=' ')
        salary = int(tmp_line[1])
        if salary < 20000:
            print(tmp_line[0])
        sum_salary += int(salary)
        employees += 1
print(sum_salary/employees)

