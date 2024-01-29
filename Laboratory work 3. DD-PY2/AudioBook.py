from Book import Book


class AudioBook(Book):
    """Класс производный от класса Book"""
    def __init__(self, name: str, author: str, duration: float):
        """Инициализируем аудио книгу"""
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"

    @property
    def duration(self) -> float:
        """Возвращаем продолжительность аудио книги"""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливаем продолжительность аудио книге"""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудио книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудио книги должна быть положительным числом")
        self._duration = new_duration
