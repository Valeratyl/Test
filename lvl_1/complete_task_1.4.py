# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

#titles_keys = list(titles.keys())

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

#list_store = store [titles[titles_keys[0]]]
#print(list_store[0])
#dict_store = list_store[0]
#print(dict_store['quantity'] * dict_store['price'])

titles_keys = list(titles.keys())

for code in titles_keys:
    list_store = store [titles[code]]
    len_list = (len(list_store))
    x,sum_quantity,sum_price  = 0,0,0

    while x < len_list:        
        dict_store = list_store[x]
        quantity = dict_store['quantity']
        sum_quantity += quantity 
        prace = dict_store['price']
        sum = dict_store['quantity'] * dict_store['price']
        sum_price += sum 
        x += 1
    print(code, '-', sum_quantity, 'шт, стоимость', sum_price, 'руб.')
        
    #if len_list == 1:
        #dict_store = list_store[0]   
        #print(code, dict_store['quantity'], 'шт, стоимость', dict_store['quantity'] * dict_store['price'], 'руб.')
    #elif len_list == 2:
        #dict_store = list_store[0]
        #dict_store_1 = list_store[1]
        #print(dict_store['quantity'] * dict_store['price'] + dict_store_1['quantity'] * dict_store_1['price'])
    #else:
        #dict_store = list_store[0]
        #dict_store_1 = list_store[1]
        #dict_store_2 = list_store[2]
        #print(dict_store['quantity'] * dict_store['price'] + dict_store_1['quantity'] * dict_store_1['price'] + dict_store_2['quantity'] * dict_store_2['price'])

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

