# Инициализация данных
minutes = int(input('Введите количество минут: '))

# Вычисления
full_hour = (minutes // 60)
minutes_left = (minutes % 60)

# Вывод результата
print('Полных часов:', full_hour)
print('Осталось минут:', minutes_left)