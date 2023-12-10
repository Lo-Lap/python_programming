import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as inp:  # Открываем файл на чтение
        reader = csv.DictReader(inp)
        list_ = [row for row in reader]  # row - словарь со значениями

    with open(OUTPUT_FILENAME, 'w') as out:  # Открываем файл на запись
        json.dump(list_, out, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
