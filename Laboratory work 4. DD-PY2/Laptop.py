from ComputerBase import ComputerBase


class Laptop(ComputerBase):
    """Класс производный от класса Компьютер"""
    def __init__(self, model: str, year_of_issue: int, price: int, diagonal: float):
        """
        Создание и подготовка к использованию класса Ноутбук
        :param model: модель компьютера
        :param year_of_issue: год создания компьютера
        :param price: текущая стоимость компьютера
        :param diagonal: диагональ ноутбука

        Attributes:
            _model: непубличный аттрибут, так как модель компьютера нельзя изменять
                    (и будет создан только геттер этого аттрибута)
            _year_of_issue: непубличный аттрибут, так как год создания компьютера нельзя изменять
                        (и будет создан только геттер этого аттрибута)
            price: публичный аттрибут, так как текущая стоимость компьютера может изменяться с течением времени
            _diagonal: непубличный аттрибут, так как диагональ ноутбука нельзя изменять
                        (и будет создан только геттер этого аттрибута)
        """
        super().__init__(model, year_of_issue, price)
        self._diagonal = diagonal

    def __repr__(self) -> str:
        """Перегружаем магический метод repr базового класса ComputerBase, так как для для создания
             экземпляра класса Laptop ранее уже создаваемого, нужно указать ещё и диагональ"""
        return f"{self.__class__.__name__}(model={self._model!r}, year_of_issue={self._year_of_issue}, " \
               f"price = {self.price}, diagonal={self._diagonal})"

    def information(self) -> None:
        """Выводим информацию об экземпляре класса

        Перегружаем метод information, так как для ноутбука появляется
            ещё информация о диагонали ноутбука"""

        print("Информация о ноутбуке:")
        print(f"Модель компьютера: {self._model}")
        print(f"Год создания компьютера: {self._year_of_issue}")
        print(f"Текущая стоимость компьютера: {self._price}")
        print(f"Диагональ ноутбука: {self._diagonal}")

    @property
    def diagonal(self) -> float:
        """Геттер для диагонали ноутбука, чтобы сделать атрибут diagonal только для чтения"""
        return self._diagonal

