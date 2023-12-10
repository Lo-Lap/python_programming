import doctest


class Vet_passport:
    def __init__(self, type_animal: str, breed: str, nickname: str, year_of_birth: int, number_of_vaccinations: int):
        """
        Создание и подготовка к работе объекта Ветеринарный паспорт
        :param type_animal: вид животного
        :param breed: порода животного
        :param nickname: кличка животного
        :param year_of_birth: год рождения животного
        :param number_of_vaccinations: количество сделанных вакцинаций

        Пример:
        >>> vet_passport = Vet_passport("Кот", "Дворовой", "Рыжий", 2007, 0)  # инициализация экземпляра класса
        ...
        """

        if not isinstance(type_animal, str):
            raise TypeError("Вид животного должен быть типа str")
        self.type_animal = type_animal

        if not isinstance(breed, str):
            raise TypeError("Порода животного должна быть типа str")
        self.breed = breed

        if not isinstance(nickname, str):
            raise TypeError("Кличка животного должна быть типа str")
        self.nickname = nickname

        if not isinstance(year_of_birth, int):
            raise TypeError("Год рождения должен быть int")
        if year_of_birth < 0:
            raise ValueError("Год рождения не может быть отрицательным числом")
        self.year_of_birth = year_of_birth

        if not isinstance(number_of_vaccinations, int):
            raise TypeError("Количество вакцинаций должно быть int")
        if number_of_vaccinations < 0:
            raise ValueError("Количество вакцинаций не может быть отрицательным числом")
        self.number_of_vaccinations = number_of_vaccinations

    def info_about_animal(self) -> None:
        """
        Выводит информации о животном из ветеринарного пасспорта

        Пример:
        >>> vet_passport = Vet_passport("Кот", "Дворовой", "Рыжий", 2007, 0)  # инициализация экземпляра класса
        >>> vet_passport.info_about_animal()
        ...
        """
        ...

    def rename_animal(self, new_name: str) -> None:
        """
        Изменяем кличку животного (если ранее была допущена ошибка)
        :param new_name: новая кличка животного

        Пример:
        >>> vet_passport = Vet_passport("Кот", "Дворовой", "Рижий", 2007, 0)  # инициализация экземпляра класса
        >>> vet_passport.rename_animal("Рыжий")
        ...
        """

        if not isinstance(new_name, str):
            raise TypeError("Новая кличка животного должна быть типа str")
        ...

    def add_vaccination(self, count_vaccination):
        """
        Добавляем количество ещё сделанных вакцинаций
        :param count_vaccination: количество ещё сделанных вакцинаций
        :raise ValueError: Если количество ещё сделанных вакцинаций отрицательное число, то вызываем ошибку

        Пример:
        >>> vet_passport = Vet_passport("Кот", "Дворовой", "Рыжий", 2007, 0)  # инициализация экземпляра класса
        >>> vet_passport.add_vaccination(4)
        ...
        """

        if not isinstance(count_vaccination, int):
            raise TypeError("Количество ещё сделанных вакцинаций должно быть int")
        if count_vaccination < 0:
            raise ValueError("Количество ещё сделанных вакцинаций не может быть отрицательным числом")

        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
