from Book import Book


class PaperBook(Book):
    """Класс производный от класса Book"""
    def __init__(self, name: str, author: str, pages: int):
        """Инициализируем бумажную книгу"""
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"

    @property
    def pages(self) -> int:
        """Возвращаем количество страниц в бумажной книги"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливаем количество страниц в бумажной книге"""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages
