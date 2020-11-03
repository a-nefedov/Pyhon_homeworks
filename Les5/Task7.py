"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
with open('FileTask7.txt', "r", encoding='UTF-8') as file:
    profit = 0
    count = 0
    firm_dict = {}
    for line in file.readlines():
        my_list = line.split(sep=' ')
        tmp_dict = {my_list[0]: int(my_list[2])-int(my_list[3])}
        firm_dict.update(tmp_dict)
        if int(my_list[2]) > int(my_list[3]):
            profit += (int(my_list[2])-int(my_list[3]))
            count += 1
    average_profit = profit / count
    new_dict = {'average_profit': average_profit}
    list_for_json = [firm_dict, new_dict]

with open("my_file.json", "w") as write_f:
    json.dump(list_for_json, write_f)
