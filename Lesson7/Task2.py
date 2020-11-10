"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Coat(Clothes):

    def __init__(self, size):
        super().__init__('Пальто')
        self.__size = size

    @property
    def size(self):
        return self.__size

    def calc_cloth_size(self):
        return self.__size / 6.5 + 0.5

    def __str__(self):
        return f'Размер = {self.__size}'


class Suit(Clothes):

    def __init__(self, height):
        super().__init__('Костюм')
        self.__height = height

    @property
    def height(self):
        return self.__height

    def calc_cloth_size(self):
        return 2 * self.__height + 0.3

    def __str__(self):
        return f'Размер = {self.__height}'


cloth_a = Suit(35)
cloth_b = Coat(46)
print(cloth_a.calc_cloth_size())
print(cloth_b.calc_cloth_size())
