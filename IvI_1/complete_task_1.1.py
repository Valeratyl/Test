# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Столбиком.
print('\n',my_favorite_songs[ :14],'\n',my_favorite_songs[-13: ],'\n',my_favorite_songs[16:30],'\n',my_favorite_songs[-26:-15])
# В строку.
print('\n',my_favorite_songs[ :14], my_favorite_songs[-13: ], my_favorite_songs[16:30], my_favorite_songs[-26:-15])

