# Функция поиска общих участников
# first_group-первая группа участников, second_group - вторая группа, delimiter - разделитель строки
def find_common_participants(first_group, second_group, delimiter=","):
    first_group_list = first_group.split(delimiter)  # Разделяем строку по разделителю
    second_group_list = second_group.split(delimiter)  # Разделяем строку по разделителю

    # Определяем общих участников и формируем из них список:
    common_participants = list(set(first_group_list).intersection(second_group_list))
    common_participants.sort()  # Сортируем получившийся список

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, delimiter="|"))
