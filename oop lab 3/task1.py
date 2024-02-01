class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        использован префикс __ для обозначения приватности,
        чтобы не позволить менять атриибуты.
        Для обращения необходимо использовать _Book__name.
        По идеи надо было использовать protected, но с префиксом _
        все еще можно менять значение атрибута для экземпляра
        """
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленным")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленным")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._Book__name!r}, author={self._Book__author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типом float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительна")
        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типом float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительна")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._Book__name!r}, author={self._Book__author!r}, duration={self.duration})"


audio = AudioBook("master", "Bulgakov", 1.05)
paper = PaperBook("war", "Tolst", 450)
print(audio.__repr__())
print(paper.__repr__())
