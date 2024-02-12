from ComputerBase import ComputerBase


class DesktopComputer(ComputerBase):
    """Класс производный от класса Компьютер"""

    def __init__(self, model: str, year_of_issue: int, price: int, installation_location: str):
        """
        Создание и подготовка к использованию класса Стационарный компьютер
        :param model: модель компьютера
        :param year_of_issue: год создания компьютера
        :param price: текущая стоимость компьютера
        :param installation_location: место установки компьютера (например, офис)

        Attributes:
            _model: непубличный аттрибут, так как модель компьютера нельзя изменять
                    (и будет создан только геттер этого аттрибута)
            _year_of_issue: непубличный аттрибут, так как год создания компьютера нельзя изменять
                        (и будет создан только геттер этого аттрибута)
            price: публичный аттрибут, так как текущая стоимость компьютера может изменяться с течением времени
            installation_location: публичный аттрибут, так как место установки компьютера может быть изменено
        """
        super().__init__(model, year_of_issue, price)
        self.installation_location = installation_location

    def __repr__(self) -> str:
        """Перегружаем магический метод repr базового класса ComputerBase, так как для создания
             экземпляра класса DesktopComputer ранее уже создаваемого, нужно указать ещё и место установки"""
        return f"{self.__class__.__name__}(model={self._model!r}, year_of_issue={self._year_of_issue}, " \
               f"price = {self._price}, installation_location={self._installation_location!r})"

    def information(self) -> None:
        """Выводим информацию об экземпляре класса

        Перегружаем метод information, так как для стационарного компьютера появляется
            ещё информация о месте установки компьютера"""

        print("Информация о стационарном компьютере:")
        print(f"Модель компьютера: {self._model}")
        print(f"Год создания компьютера: {self._year_of_issue}")
        print(f"Текущая стоимость компьютера: {self._price}")
        print(f"Место установки компьютера: {self._installation_location}")

    @property
    def installation_location(self) -> str:
        """Геттер для места установки компьютера , чтобы сделать атрибут installation_location только для чтения"""
        return self._installation_location

    @installation_location.setter
    def installation_location(self, new_installation_location: str) -> None:
        """
        Устанавливаем место установки компьютера
        :param new_installation_location: место установки стационарного компьютера
        """
        if not isinstance(new_installation_location, str):
            raise TypeError("Место установки компьютера должно быть типа str")
        self._installation_location = new_installation_location

