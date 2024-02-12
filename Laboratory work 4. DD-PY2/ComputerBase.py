

class ComputerBase:
    """Базовый класс компьютера"""
    def __init__(self, model: str, year_of_issue: int, price: int):
        """
        Инициализация объекта базового класса Компьютера

        :param model: модель компьютера
        :param year_of_issue: год создания компьютера
        :param price: текущая стоимость компьютера

        Attributes:
            _model: непубличный аттрибут, так как модель компьютера нельзя изменять
                    (и будет создан только геттер этого аттрибута)
            _year_of_issue: непубличный аттрибут, так как год создания компьютера нельзя изменять
                            (и будет создан только геттер этого аттрибута)
            price: публичный аттрибут, так как текущая стоимость компьютера может изменяться с течением времени
        """
        self._model = model
        self._year_of_issue = year_of_issue
        self.price = price

    def __str__(self) -> str:
        """Определяем поведение функции str(), вызванной для экземпляра класса"""
        return f"Модель компьютера {self._model}. Год создания {self._year_of_issue}. Текущая стоимость {self._price}"

    def __repr__(self) -> str:
        """Определяем поведение функции repr(), вызванной для экземпляра класса"""
        return f"{self.__class__.__name__}(model={self._model!r}, year_of_issue={self._year_of_issue}, " \
               f"price = {self._price})"

    def change_in_price_on(self, change: int) -> None:
        """
        Изменение стоимости компьютера на величину change
        :param change: величина на сколько изменяем стоимость компьютера

        Если change - отрицательная величина, то уменьшаем стоимость
        Если change - положительная величина, то увеличиваем стоимость
        """
        if not isinstance(change, int):
            raise TypeError("Величина change должна быть типа int")
        if self._price + change < 0:
            raise ValueError("Величина уменьшающая стоимость компьютера не может по модулю "
                             "превышать стоимость компьютера")
        self.price = self._price + change
        print("Стоимость изменена")

    def information(self) -> None:
        """Выводим информацию об экземпляре класса"""
        print("Информация о компьютере:")
        print(f"Модель компьютера: {self._model}")
        print(f"Год создания компьютера: {self._year_of_issue}")
        print(f"Текущая стоимость компьютера: {self._price}")

    @property
    def model(self) -> str:
        """Геттер для модели компьютера, чтобы сделать атрибут model только для чтения"""
        return self._model

    @property
    def year_of_issue(self) -> int:
        """Геттер для года создания компьютера, чтобы сделать атрибут year_of_issue только для чтения"""
        return self._year_of_issue

    @property
    def price(self) -> int:
        """Возвращаем текущую стоимость компьютера"""
        return self._price

    @price.setter
    def price(self, new_price: int) -> None:
        """
        Устанавливаем текущую стоимость компьютера
        :param new_price: устанавливаемая стоимость компьютера
        """
        if not isinstance(new_price, int):
            raise TypeError("Текущая стоимость компьютера должна быть типа int")
        if new_price <= 0:
            raise ValueError("Текущая стоимость компьютера должна быть положительным числом")
        self._price = new_price
