# Ввод количества заказов
orders_count = int(input('Введите количество заказов: '))

# Создаем пустой словарь для хранения данных о заказах
database = dict()

# Обрабатываем каждый заказ
for i_order in range(orders_count):
    # Вводим заказ и разбиваем его на части
    customer, pizza_name, count = input('{} заказ: '.format(i_order + 1)).split()
    
    # Преобразуем количество в целое число
    count = int(count)
    
    # Если покупатель еще не добавлен в словарь
    if customer not in database:
        # Добавляем покупателя и начальную запись о пицце
        database[customer] = {pizza_name: count}
    else:
        # Если покупатель уже есть
        if pizza_name in database[customer]:
            # Если пицца уже была заказана ранее, увеличиваем количество
            database[customer][pizza_name] += count
        else:
            # Если пицца новая для этого покупателя, добавляем запись
            database[customer][pizza_name] = count

# Сортируем список покупателей в алфавитном порядке и выводим информацию
for customer in sorted(database.keys()):
    print('{}:'.format(customer))
    # Сортируем пиццы по алфавиту и выводим информацию
    for pizza_name in sorted(database[customer].keys()):
        print(' {}: {}'.format(pizza_name,
database[customer][pizza_name]))