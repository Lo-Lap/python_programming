
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        """Геттер для названия книги, чтобы сделать атрибут name только для чтения"""
        return self._name

    @property
    def author(self) -> str:
        """Геттер для автора книги, чтобы сделать атрибут author только для чтения"""
        return self._author
