class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.__validate_pages(pages)
        self.__pages = pages

    @staticmethod
    def __validate_pages(pages: int):
        if not isinstance(pages, int):
            raise TypeError()
        if not pages > 0:
            raise ValueError()

    @property
    def pages(self):
        return self.__pages

    def __str__(self):
        return Book.__str__(self) + f"Количество страниц {self.pages}"

    def __repr__(self):
        return Book.__repr__(self) + f" pages={self.__pages!r}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.__validate_duration(duration)
        self.__duration = duration

    @staticmethod
    def __validate_duration(duration: float):
        if not isinstance(duration, float):
            raise TypeError()
        if not duration > 0:
            raise ValueError()

    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        return Book.__str__(self) + f"Продолжительность {self.duration}"

    def __repr__(self):
        return Book.__repr__(self) + f" duration={self.__duration!r}"


