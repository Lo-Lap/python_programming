
class Book():
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта Книга
        :param id_: идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть int")
        if id_ < 0:
            raise ValueError("Идентификатор книги не может быть отрицательным числом")
        self.id = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть int")
        if pages < 0:
            raise ValueError("Количество страниц в книге не может быть отрицательным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


if __name__ == "__main__":
    book = Book(1, "Красавица и чудовище", 40)
    print(str(book))
    print(repr(book))
