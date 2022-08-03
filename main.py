

# Задание1
# Должен получится следующий словарь

#advice - Задача 1 - вы забыли что есть строка разделитель, а значит надо делать “фейковое чтение” строки -
# вам бы помогло использование отдладчика, вы бы увидели как и куда движется ваш код.
# "for line in file_work:
#             dish_name = <что-то тут делаем>
#             counter = <как-то получили кол-во строк>
#             list_of_ingridient = <временный список>
#             for i in <наш счетчик counter использовать range>:
#                 temp_dict = {} - временный словарь
#                 ingridient = file_work.readline() - вот так перемещаемся по файлу
#                 <заполняем словарь с ингридиетом>
#                 <добавляем словарь в список>
#             <записываем в словарь cook_dict наш рецепт>
#             file_work.readline() - еще раз смещаетмся т.к. там пустая срока"

def open_file():
    cook_book = {}
    # ingredients_list = []
    with open('recipes.txt','r') as f:
       for line in f:
          dish_name = line.strip()
          #dish_name = f.readline().strip()
          ingredients_qty = int(f.readline().strip())
          ingredients_list = []
          # print(dish_name)
          # print(ingredients_qty)
       # print(dish_name)
       # print(ingredients_qty)
          for ingredient_line in range(ingredients_qty):
              ingredient_dict_temp = {}
              item1, item2, item3 = f.readline().split("|")
              ingredient_dict_temp['ingredient_name'] = item1.strip(' ')
              ingredient_dict_temp['quantity'] = item2.strip(' ')
              ingredient_dict_temp['measure'] = item3.strip(' \n')
              ingredients_list.append(ingredient_dict_temp)
          cook_book[dish_name] = ingredients_list
          f.readline()
       print(cook_book)
open_file()
print()
print()
print()
# Задание2
#кулинарная книга из задания 1
cook_book = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'}, {'ingredient_name': 'Молоко', 'quantity': '100', 'measure': 'мл'}, {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}], 'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': '1', 'measure': 'шт'}, {'ingredient_name': 'Вода', 'quantity': '2', 'measure': 'л'}, {'ingredient_name': 'Мед', 'quantity': '3', 'measure': 'ст.л'}, {'ingredient_name': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}], 'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'}, {'ingredient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч'}, {'ingredient_name': 'Сыр гауда', 'quantity': '100', 'measure': 'г'}], 'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': '500', 'measure': 'г'}, {'ingredient_name': 'Перец сладкий', 'quantity': '1', 'measure': 'шт'}, {'ingredient_name': 'Лаваш', 'quantity': '2', 'measure': 'шт'}, {'ingredient_name': 'Винный уксус', 'quantity': '1', 'measure': 'ст.л'}, {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}]}
 # Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон
 # для кого мы будем готовить  get_shop_list_by_dishes(dishes, person_count)
 # На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда.
 # Например, для такого вызова get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
 # Должен быть следующий результат:
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}}
# Обратите внимание, что ингредиенты могут повторяться

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_ingredients = {}

    for dish, ingredients_list in cook_book.items():
        if dish in dishes:
            for item in ingredients_list:
                shop_list_qty_temp = {} #temporary dictionary for collection of ingredients measure and qty in loop
                shop_item = item['ingredient_name']
                shop_measure = item['measure']
                shop_qty = int(item['quantity']) * int(person_count)
                shop_list_qty_temp['measure'] = shop_measure
                shop_list_qty_temp['quantity'] = shop_qty
                shop_list_ingredients[shop_item] = shop_list_qty_temp
    print(shop_list_ingredients)
get_shop_list_by_dishes(['Омлет','Запеченный картофель'],2)
print()
print()

# Задание №3
# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны,
# пример для выполнения домашней работы можно взять тут. Необходимо объединить их в один по следующим правилам:
# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
# Пример
# Даны файлы: 1.txt
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 2.txt
# Строка номер 1 файла номер 2
# Итоговый файл:
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

def combine_files():
    import os, fnmatch
    files = fnmatch.filter(os.listdir('.'), '*_.txt')
    print(files)
    print()
    files_combined = {}
    file_data = []
    for file in files:
        with open(file) as f:
            data = f.readlines()
            data_len = len(data)
            print(data_len)
            file_data.append(data_len)
            file_data.append(data)
            files_combined[file] = file_data
            file_data = []
    print()
    print(files_combined)
    files_sorted = sorted(files_combined.items(), key=lambda kv: (kv[1], kv[0]))
    print()
    files_sorted_ = list(files_sorted)
    print(files_sorted_)
    print()

    with open('result.txt', 'w') as f_:
        for item in files_sorted_:
            f_.write(str(item[0]))
            f_.write('\n')
            f_.write(str(item[1][0]))
            f_.write('\n')
            f_.write(str(item[1][1]))
            f_.write('\n')
            f_.write('\n')
    f_.close()
combine_files()


