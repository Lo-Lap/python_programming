import doctest


class School:
    def __init__(self, school_name: str, year_of_foundation: int, number_of_teachers: int, number_of_students: int):
        """
        Создание и подготовка к работе объекта Школа
        :param school_name: название школы
        :param year_of_foundation: год основания школы
        :param number_of_teachers: количество учителей в школе
        :param number_of_students: количество учеников в школе

        Пример:
        >>> school = School("№16", 1990, 100, 1000)  # инициализация экземпляра класса
        ...
        """

        if not isinstance(school_name, str):
            raise TypeError("Название школы должно быть типа str")
        self.school_name = school_name

        if not isinstance(year_of_foundation, int):
            raise TypeError("Год основания должен быть int")
        if year_of_foundation < 0:
            raise ValueError("Год основания не может быть отрицательным числом")
        self.year_of_foundation = year_of_foundation

        if not isinstance(number_of_teachers, int):
            raise TypeError("Количество учителей должно быть int")
        if number_of_teachers < 0:
            raise ValueError("Количество учителей в школе не может быть отрицательным числом")
        self.number_of_teachers = number_of_teachers

        if not isinstance(number_of_students, int):
            raise TypeError("Количество учеников должно быть int")
        if number_of_students < 0:
            raise ValueError("Количество учеников в школе не может быть отрицательным числом")
        self.number_of_students = number_of_students

    def rename_school(self, new_school_name: str) -> None:
        """
        Переименовывание школы
        :param new_school_name: новое название школы

        Пример:
        >>> school = School("№16", 1990, 100, 1000)  # инициализация экземпляра класса
        >>> school.rename_school("Гимназия №16")
        ...
        """

        if not isinstance(new_school_name, str):
            raise TypeError("Новое название школы должно быть типа str")
        ...

    def add_teacher(self, count_teachers: int) -> None:
        """
        Пришедшие учителя в школу
        :param count_teachers: количество пришедших в школу учителей
        :raise ValueError: Если количество пришедших учителей отрицательное число, то вызываем ошибку

        Пример:
        >>> school = School("№16", 1990, 100, 1000)  # инициализация экземпляра класса
        >>> school.add_teacher(5)
        ...
        """

        if not isinstance(count_teachers, int):
            raise TypeError("Количество пришедших учителей должно быть int")
        if count_teachers < 0:
            raise ValueError("Количество пришедших учителей в школу не может быть отрицательным числом")

        ...

    def add_students(self, count_students: int) -> None:
        """
        Пришедшие ученики в школу
        :param count_students: количество пришедших в школу учеников
        :raise ValueError: Если количество пришедших учеников отрицательное число, то вызываем ошибку

        Пример:
        >>> school = School("№16", 1990, 100, 1000)  # инициализация экземпляра класса
        >>> school.add_students(5)
        ...
        """

        if not isinstance(count_students, int):
            raise TypeError("Количество пришедших учеников должно быть int")
        if count_students < 0:
            raise ValueError("Количество пришедших учеников в школу не может быть отрицательным числом")
        ...

    def teachers_who_left_school(self, count_teachers):
        """
        Ушедшие из школы учителя
        :param count_teachers: Количество ушедших из школы учителей
        :raise ValueError: Если количество ушедших из школы учителей отрицательное число, то вызываем ошибку
        :raise ValueError: Если количество ушедших из школы учителей превышает текущее количество учителей в школе,
        то вызываем ошибку

        Пример:
        >>> school = School("№16", 1990, 100, 1000)  # инициализация экземпляра класса
        >>> school.teachers_who_left_school(5)
        ...
        """

        if not isinstance(count_teachers, int):
            raise TypeError("Количество ушедших из школы учителей должно быть int")
        if count_teachers < 0:
            raise ValueError("Количество ушедших из школы учителей не может быть отрицательным числом")
        if count_teachers > self.number_of_teachers:
            raise ValueError("Количество ушедших из школы учителей не может быть больше текущего количества учителей")
        ...

    def students_who_left_school(self, count_students):
        """
        Ушедшие из школы ученики
        :param count_students: Количество ушедших из школы учеников
        :raise ValueError: Если количество ушедших из школы учеников отрицательное число, то вызываем ошибку
        :raise ValueError: Если количество ушедших из школы учеников превышает текущее количество учеников в школе,
        то вызываем ошибку

        Пример:
        >>> school = School("№16", 1990, 100, 1000)  # инициализация экземпляра класса
        >>> school.students_who_left_school(5)
        ...
        """

        if not isinstance(count_students, int):
            raise TypeError("Количество ушедших из школы учеников должно быть int")
        if count_students < 0:
            raise ValueError("Количество ушедших из школы учеников не может быть отрицательным числом")
        if count_students > self.number_of_students:
            raise ValueError("Количество ушедших из школы учеников не может быть больше текущего количества учеников")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
