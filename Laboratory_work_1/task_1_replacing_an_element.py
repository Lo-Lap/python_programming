numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = 4 #индекс пропущенного элемента
# TODO заменить значение пропущенного элемента средним арифметическим
numbers_ = numbers[:missing_index]+numbers[missing_index+1:] #формируем спимок без None элемента
sum_of_numbers_ = sum(numbers_) #сумма элементов без None
count_of_numbers = len(numbers) #длина списка элементов с None
numbers[missing_index] = sum_of_numbers_/count_of_numbers #заменяем пустой элемент на среднее арифметическое
print("Измененный список:", numbers)
