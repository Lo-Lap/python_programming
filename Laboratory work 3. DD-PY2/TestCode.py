from Book import Book
from AudioBook import AudioBook
from PaperBook import PaperBook


"""Код для проверки работы методов классов"""
if __name__ == "__main__":
    book = Book("Мастер и Маргарита", "М.А. Булгаков")
    print(str(book))
    print(repr(book))

    paper_book = PaperBook("Мцыри", "М.Ю. Лермонтов", 40)
    print(str(paper_book))
    print(repr(paper_book))

    audio_book = AudioBook("Мёртвые души", "Н.В. Гоголь", 10.28)
    print(str(audio_book))
    print(repr(audio_book))
