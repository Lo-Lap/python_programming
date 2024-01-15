from Book import Book


class Library:
    def __init__(self, books: list[Book] = None):
        """
        Создание и подготовка к работе объекта Библиотека
        :param books: список книг в библиотеке
        """

        if books is None:
            self.books = []
        else:
            if not isinstance(books, list):
                raise TypeError("Список книг в библиотеке должен быть list")

            if not all(isinstance(x, Book) for x in books):
                raise TypeError("Все элементы списка должны быть типа Book")
            self.books = books

    def get_next_book_id(self) -> int:
        """
        Функция, возвращающая идентификатор для добавления новой книги в библиотеку
        :return: идентификатор последней книги увеличенной на 1
        """
        if not self.books:
            return 1
        else:
            # self.books[-1].id вернёт id последнего элемента в списке
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id_) -> int:
        """
        Функция для возврата индекса книги в списке по id книги
        :param id_: id книги
        :return: индекс книги в списке книг books_
        """

        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть int")
        if id_ < 0:
            raise ValueError("Идентификатор книги не может быть отрицательным числом")

        for index, book_ in enumerate(self.books):
            if book_.id == id_:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")

    def add_book(self, book_: Book):
        """
        Функция для добавления книги в библиотеку
        :param book_: книга, которую нужно добавить
        """
        if not isinstance(book_, Book):
            raise TypeError("Добавляемая книга должна быть типа Book")

        self.books.append(book_)


if __name__ == "__main__":
    book = Book(1, "Красавица и чудовище", 40)
    lib1 = Library()
    print("id в пустой библиотеке: ", lib1.get_next_book_id())
    book2 = Book(lib1.get_next_book_id(), "Поэмы", 400)
    lib1.add_book(book2)
    book3 = Book(lib1.get_next_book_id(), "Архитектура", 200)
    lib1.add_book(book3)
    print("Индекс книги с id = 2: ", lib1.get_index_by_book_id(2))

    lib2 = Library([book, book3])
    print("id для следующей книги во второй библиотеке:", lib2.get_next_book_id())
    lib2.get_index_by_book_id(1)

