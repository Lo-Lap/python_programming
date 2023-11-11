import json


def task() -> float:
    with open('input.json') as file:  # Открываем файл на чтение
        data_in_json = json.load(file)  # Считываем данные из файла

    # Составляем список из произведений чисел из словаря по значениям "score" и "weight"
    list_product = [data["score"]*data["weight"] for data in data_in_json]

    return round(sum(list_product), 3)  # Суммируем числа из списка и округляем её


print(task())
