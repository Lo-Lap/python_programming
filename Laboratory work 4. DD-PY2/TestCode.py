from ComputerBase import ComputerBase
from DesktopComputer import DesktopComputer
from Laptop import Laptop


if __name__ == "__main__":
    # Пример использования класса ComputerBase
    baseComputer = ComputerBase("DEXP Aquilon O289", 2022, 16000)
    print(str(baseComputer))
    baseComputer.change_in_price_on(50)
    print(repr(baseComputer))
    baseComputer.information()
    print()

    # Пример использования класса DesktopComputer
    deckComputer = DesktopComputer("DEXP Atlas H417", 2023, 20000, "офис")
    print(str(deckComputer))
    deckComputer.change_in_price_on(-400)
    print(repr(deckComputer))
    deckComputer.information()
    print()

    # Пример использования класса Laptop
    laptop = Laptop("DEXP Aquilon", 2022, 18000, 14.1)
    print(str(laptop))
    laptop.change_in_price_on(100)
    print(repr(laptop))
    laptop.information()
