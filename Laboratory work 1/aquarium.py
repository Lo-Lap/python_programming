import doctest


class Aquarium:
    def __init__(self, volume_of_aquarium: float, occupied_volume: float, count_fish: int):
        """
        Создание и подготовка к работе объекта Аквариум
        :param volume_of_aquarium: объём аквариума
        :param occupied_volume: объем аквариума, занятый водой
        :param count_fish: количество рыб в аквариуме

        Примеры:
        >>> aquarium = Aquarium(500, 400, 10)  # инициализация экземпляра класса
        ...
        """
        if not isinstance(volume_of_aquarium, (int, float)):
            raise TypeError("Объем аквариума должен быть типа int или float")
        if volume_of_aquarium <= 0:
            raise ValueError("Объем аквариума должен быть положительным числом")
        self.volume_of_aquarium = volume_of_aquarium

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объём воды в аквариуме должен быть int или float")
        if occupied_volume < 0:
            raise ValueError("Объём воды в аквариуме не может быть отрицательным числом")
        if occupied_volume > volume_of_aquarium:
            raise ValueError("Объём воды в аквариуме не может превышать объёма всего аквариума")
        self.occupied_volume = occupied_volume

        if not isinstance(count_fish, int):
            raise TypeError("Количество рыб в аквариуме должно быть int")
        if count_fish < 0:
            raise ValueError("Количество рыб в аквариуме не может быть отрицательным числом")
        if occupied_volume == 0 & count_fish != 0:
            raise ValueError("Количество рыб в пустом аквариуме не может быть больше нуля")
        self.count_fish = count_fish

    def aquarium_is_empty(self) -> bool:
        """
        Проверка на пустоту оквариума по объёму воды в нём
        :return: Является ли аквариум пустым

        Примеры:
        >>> aquarium = Aquarium(500, 400, 10)  # инициализация экземпляра класса
        >>> aquarium.aquarium_is_empty()
        ...
        """
        ...

    def add_fish_to_aquarium(self, fish: int) -> None:
        """
        Добавление рыб в аквариум
        :param fish: количество добавляемых рыб в аквариум
        :raise ValueError: Если количество добавляемых в аквариум рыб - отрицательное число, то вызываем ошибку

        Примеры:
        >>> aquarium = Aquarium(500, 400, 10)  # инициализация экземпляра класса
        >>> aquarium.add_fish_to_aquarium(5)
        ...
        """
        if not isinstance(fish, int):
            raise TypeError("Количество добавляемых рыб в аквариум должно быть int")
        if fish < 0:
            raise ValueError("Количество добавляемых рыб в аквариум не может быть отрицательным числом")
        ...

    def remove_fish_from_aquarium(self, remove_fish) -> None:
        """
        Убираем рыб из аквариума
        :param remove_fish: количество убираемых рыб из аквариума
        :raise ValueError: Если количество удаляемых из аквариума рыб - отрицательное число, то вызываем ошибку
        :raise ValueError: Если аквариум пустой, то вызываем ошибку
        :raise ValueError: Если количество удаляемых рыб из аквариума превышает количество рыб в аквариуме,
        то вызываем ошибку

        Примеры:
        >>> aquarium = Aquarium(500, 400, 10)  # инициализация экземпляра класса
        >>> aquarium.remove_fish_from_aquarium(5)
        ...
        """

        if not isinstance(remove_fish, int):
            raise TypeError("Количество удаляемых рыб из аквариума должно быть int")
        if remove_fish < 0:
            raise ValueError("Количество удаляемых рыб из аквариума не может быть отрицательным числом")
        if self.occupied_volume == 0:
            raise ValueError("Невозможно забрать рыб из пустого аквариума")
        if remove_fish > self.count_fish:
            raise ValueError("Невозможно забрать рыб больше, чем их есть в аквариуме")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
