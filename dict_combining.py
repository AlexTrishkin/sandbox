"""
Даны 2 рецепта в виде словарей продуктов и количеством необходимых продуктов,
Необходимо создать список общих продуктов и их количества, вывести их на экран
"""
pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}


def print_shopping_list(dish1, dish2):
    dishKeys1 = set(dish1.keys())  # Конвентируем ключи словаря 1 в множество
    dishKeys2 = set(dish2.keys())  # Конвентируем ключи словаря 2 в множество
    regs_list = dishKeys1.union(dishKeys2)  # добавляем в множество 1 , уникальные значения из множества 2
    for key in regs_list:  # Для ключа в множестве значений
        if key in dish1 and key in dish2:  # Если ключ находится и в 1, и во 2 словаре
            val_sum = dish1[key] + dish2[key]   # Складываем значения данного ключа из обоих словарей
            print('{}: {}'.format(key, str(val_sum)))  # Выводим на экран полученное значение ( Прим.'помидоры, кг: 2 ')
        elif key in dish1 and key not in dish2:  # Если ключ находится только в 1 словаре
            print('{}: {}'.format(key, str(dish1[key])))  # Выводим его значение
        else:
            print('{}: {}'.format(key, str(dish2[key])))  # Иначе выводи значение ключа из 2 словаря


print_shopping_list(pizza, salad)