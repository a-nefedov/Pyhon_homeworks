"""
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

user_list = []
index = 1

while True:
    user_list.append((index, {"Название": input('Введите название товара'),
                            "Цена": input('Введите цену товара'),
                            "Количество": input('Введите количество товара'),
                            "Ед": input('Введите еденицу измерения ')}))
    if input('Для завершения ввода, введите q') == 'q':
        break
    index += 1


name = []
price = []
cnt = []
unit = []

tmp = 0

while tmp < index:
    name.append(my_list[tmp][1].get("Название"))
    price.append(my_list[tmp][1].get("Цена"))
    cnt.append(my_list[tmp][1].get("Количество"))
    unit.append(my_list[tmp][1].get("Ед"))
    tmp += 1

print({"Название": list(set(name)),
       "Цена": list(set(price)),
       "Количество": list(set(cnt)),
       "Ед": list(set(unit))})
