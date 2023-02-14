class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._new_pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if pages < 0:
            raise ValueError('Количество страниц меньше 0')
        if type(pages) != int:
            raise TypeError('Требуется целочисленное значение')
        self._new_pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})'

    @property
    def duration(self) -> float:
        return self._new_duration

    @duration.setter
    def duration(self, value) -> None:
        if value < 0:
            raise ValueError('Длительность аудиокниги меньше 0')
        if type(value) != float:
            raise TypeError('Требуется число с плавающей запятой')
        self._new_duration = value


ebook = AudioBook(name='Name', author='Author', duration=1.0)
paper = PaperBook(name='P', author='IA', pages=123)
print(ebook)
print(paper)
