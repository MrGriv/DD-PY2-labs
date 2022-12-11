import doctest
from typing import Union

class Bicycle:

    def __init__(self, speed: int, brakes: str, wheel_size: Union[int, float]):
        """
        Создание и подготовка к работе объекта велосипед

        :param speed: количество скоростей заднего переключателя
        :param brakes: система тормозов
        :param wheel_size: размер колес

        Пример:
        >>> bike26 = Bicycle(12, 'Disk', 27.5)  # инициализация экземпляра класса
        """
        self.speed = 10
        self.init_bicycle_sp(speed)
        self.brakes = 'Disk'
        self.init_brakes_sis(brakes)
        self.wheel_size = 29
        self.init_wheel_size(wheel_size)

    def init_bicycle_sp(self, speed):
        """
        инициализация скоростей велосипеда

        :param speed: скорости велосипеда
        :return: скорости велосипеда
        """
        if not isinstance(speed, int):
            raise TypeError
        if speed < 0:
            raise ValueError
        self.speed = speed

    def init_brakes_sis(self, brakes):
        """
        инициализация торсозной системы велосипеда

        :param brakes: торсозная система велосипеда
        :return: торсозная система велосипеда
        """
        if not isinstance(brakes, str):
            raise TypeError
        self.brakes = brakes

    def init_wheel_size(self, wheel_size):
        """
        инициализация размера колес велосипеда

        :param wheel_size: размер колес велосипеда
        :return: размер колес велосипеда
        """
        if not isinstance(wheel_size, (int, float)):
            raise TypeError
        if wheel_size < 0:
            raise ValueError
        self.wheel_size = wheel_size

    def change_chain(self) -> None:
        """
        Замена цепи

        :return: Новая цепь

        Пример
        >>> bike26 = Bicycle(12, 'Disk', 27.5)
        >>> bike26.change_chain()
        """
        ...
    def check_distance(self) -> int:
        """
        Проверка пройденного расстояние

        :return: расстояние

        Пример
        >>> bike26 = Bicycle(12, 'Disk', 27.5)
        >>> bike26.check_distance()
        """
        ...

class SelfTappingScrew:

    def __init__(self, size: int, type_of_screw: str, color: str):
        """
        Создание и подготовка к работе объекта саморез

        :param size: Размер самореза
        :param type_of_screw: Тип самореза
        :param color: Цвет самореза

        Пример
        >>> metal_screw = SelfTappingScrew(25, 'For metal', 'White')
        """
        self.size = 45
        self.init_size(size)
        self.type_of_screw = 'For wood'
        self.init_type(type_of_screw)
        self.color = 'Black'
        self.init_color(color)

    def init_size(self, size):
        """
        Инициализация размера самореза

        :param size: размер самореза
        :return: размер самореза
        """
        if not isinstance(size, int):
            raise TypeError
        if size < 0:
            raise ValueError
        self.size = size

    def init_type(self, type_of_screw):
        """
        Инициализация типа самореза

        :param type_of_screw: тип самореза
        :return: тип самореза
        """
        if not isinstance(type_of_screw, str):
            raise TypeError
        self.type_of_screw = type_of_screw

    def init_color(self, color):
        """
        Инициализация цвета самореза

        :param color: цвет самореза
        :return: цвет самореза
        """
        if not isinstance(color, str):
            raise TypeError
        self.color = color

    def use_self_tapping_screw(self) -> None:
        """
        Использование самореза

        :return: Закрученный саморез

        Пример
        >>> metal_screw = SelfTappingScrew(25, 'For metal', 'White')
        >>> metal_screw.use_self_tapping_screw()
        """
        ...

    def count_screws(self) -> int:
        """
        Пересчет саморезов

        :return: количество саморезов

        Пример
        >>> metal_screw = SelfTappingScrew(25, 'For metal', 'White')
        >>> metal_screw.count_screws()
        """
        ...

class Apple:

    def __init__(self, color: str, amount: int):
        """
        Создание и подготовка к работе объекта яблоко

        :param color: цвет яблока
        :param amount: количество яблок

        Пример
        >>> apple = Apple('Red', 7)
        """
        self.color = 'Green'
        self.init_color(color)
        self.amount = 0
        self.init_amount(amount)

    def init_color(self, color):
        """
        Инициализация цвета яблок

        :param color: цвет яблок
        :return: цвет яблок
        """
        if not isinstance(color, str):
            raise TypeError
        self.color = color

    def init_amount(self, amount):
        """
        Инициализация количества яблок

        :param amount: количество яблок
        :return: количество яблок
        """
        if not isinstance(amount, int):
            raise TypeError
        if amount < 0:
            raise ValueError
        self.amount = amount

    def eat_apple(self) -> None:
        """
        Съесть яблоко

        :return: ничего

        Пример
        >>> apple = Apple('Red', 7)
        >>> apple.eat_apple()
        """
        ...

    def add_apples(self, amount) -> int:
        """
        Добавить яблок

        :param amount: исходное количество яблок
        :return: новое количество яблок

        Пример
        >>> apple = Apple('Red', 7)
        >>> apple.add_apples(7)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
