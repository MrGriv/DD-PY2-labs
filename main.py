if __name__ == "__main__":

    class Bicycle:
        def __init__(self, number_of_wheels: int, frame: str, size: float):
            """
            Создание базового образа велосипеда
            :param number_of_wheels: количество колес велосипеда
            :param frame: материал, из которой сделана рама велосипеда. Возможны Al, Ti, Fe, Carbon
            :param size: размер колес
            Атрибут self._wheels инкапсулирован, потому что подразумеваются только двухколесные велосипеды.
            Увеличение колес возможно, но, тогда разработчик снимает с себя ответственность за дальнейшую
            работоспособность кода.
            """
            self._wheels = number_of_wheels
            self.type_of_frame = frame
            self.wheel_size = size

        def __str__(self) -> str:
            """
            :return: вывод основной информации о велосипеде
            """
            return f"Количество колес {self._wheels}. Тип рамы {self.type_of_frame}"

        def __repr__(self) -> str:
            """
            :return: вывод всей информации о велосипеде
            """
            return f"{self.__class__.__name__}(number_of_wheels={self._wheels!r}, frame={self.type_of_frame!r}, size={self.wheel_size!r})"

        def bike_configuration(self, number_of_wheels: int, frame: str, size: float) -> None:
            """
            Конфигурация велосипеда с учетом параметров
            :param number_of_wheels: количество колес велосипеда
            :param frame: материал, из которой сделана рама велосипеда. Возможны Al, Ti, Fe, Carbon
            :param size: размер колес
            :return: модель велосипеда по сконфигурированным параметрам
            """
            ...

        def make_skin(self) -> None:
            """
            Создание модели велосипеда
            :return: прорисованная модель
            """
            ...

    class CityBike(Bicycle):
        def __init__(self, number_of_wheels: int, frame: str, size: float, bicycle_trunk: str):
            """
            Создание городского велосипеда с багажником
            :param number_of_wheels: количество колес велосипеда
            :param frame: материал, из которой сделана рама велосипеда. Возможны Al, Ti, Fe, Carbon
            :param size: размер колес
            :param bicycle_trunk: багажник велосипеда. Может быть составным или цельным(composite или full)
            Перегрузка нужна для установки багажника в стандартную модель велосипеда
            """
            super().__init__(number_of_wheels, frame, size)
            self.type_of_trunk = bicycle_trunk

        def __repr__(self) -> str:
            """
            :return: вывод всей информации о велосипеде
            """
            return f"{self.__class__.__name__}(number_of_wheels={self._wheels!r}, frame={self.type_of_frame!r}, size={self.wheel_size!r}, trunk={self.type_of_trunk!r})"

        def bike_configuration(self, number_of_wheels: int, frame: str, size: float) -> None:
            """
            Конфигурация велосипеда с учетом параметров
            :param number_of_wheels: количество колес велосипеда
            :param frame: материал, из которой сделана рама велосипеда. Возможны Al, Ti, Fe, Carbon
            :param size: размер колес
            :return: модель велосипеда по сконфигурированным параметрам
            Перегрузка нужна, чтобы учесть наличие багажника и пересчитать основные параметры рамы
            """
            super().bike_configuration(number_of_wheels, frame, size)
            ...

    class MountainBike(Bicycle):
        def __init__(self, number_of_wheels: int, frame: str, size: float, fork: str):
            """
            Создание городского велосипеда с багажником
            :param number_of_wheels: количество колес велосипеда
            :param frame: материал, из которой сделана рама велосипеда. Возможны Al, Ti, Fe, Carbon
            :param size: размер колес
            :param fork: передний амортизатор. может быть air, spring, elastomer
            Перегрузка нужна для установки переднего амортизатора в стандартную модель велосипеда
            """
            super().__init__(number_of_wheels, frame, size)
            self.fork = fork

        def __repr__(self):
            """
            :return: вывод всей информации о велосипеде
            """
            return f"{self.__class__.__name__}(number_of_wheels={self._wheels!r}, frame={self.type_of_frame!r}, size={self.wheel_size!r}, fork={self.fork!r})"

        def bike_configuration(self, number_of_wheels: int, frame: str, size: float) -> None:
            """
            Конфигурация велосипеда с учетом параметров
            :param number_of_wheels: количество колес велосипеда
            :param frame: материал, из которой сделана рама велосипеда. Возможны Al, Ti, Fe, Carbon
            :param size: размер колес
            :return: модель велосипеда по сконфигурированным параметрам
            Перегрузка нужна, чтобы учесть наличие вилки и пересчитать основные параметры рамы
            """
            super().bike_configuration(number_of_wheels, frame, size)
            ...
