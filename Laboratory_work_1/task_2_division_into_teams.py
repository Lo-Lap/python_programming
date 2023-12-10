list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_of_players = len(list_players) #определяем общее количество игроков
index_of_slice = count_of_players//2 #определяем индекс относительно которого будем производить деление участников на команды
# TODO Разделите участников на две команды

team_first = list_players[:index_of_slice] #первая команда формируется до index_of_slice
team_second = list_players[index_of_slice:] #вторая команда формируется с index_of_slice

print(team_first)
print(team_second)
