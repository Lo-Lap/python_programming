# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44 #объём дискеты в Мб
pages_in_book = 100 #количество страниц в книге
lines_per_page = 50 #количество строк на странице
string_number = 25 #количество символов в строке
storage_of_one_symbol = 4 #объём хранения одного символа в байтах

storage_of_one_symbol_in_Mb = storage_of_one_symbol/(1024*1024) #объём хранения одного символа в Мб
number_of_symbols_in_one_book = pages_in_book * lines_per_page * string_number #количество символов в одной книге
volume_of_one_book = storage_of_one_symbol_in_Mb * number_of_symbols_in_one_book # объём одной кники в Мб

count_of_books_in_disk = int(volume_disk//volume_of_one_book)

print("Количество книг, помещающихся на дискету:", count_of_books_in_disk)
