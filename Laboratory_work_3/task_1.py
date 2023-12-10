# Функция поиска индекса первого вхождения товара в список
def find_index(item_list, product):  # item_list - спиок товаров, product - товар, который нужно найти
    for index, item in enumerate(item_list):  # пронумеруем элементы списка и сравним каждый товар списка с искомым
        if item == product:  # Если нашли искомый продукт, то сразу возвражаем его индекс
            return index

    return None  # Если раньше не был вызван return, значит элемент не в списке


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
