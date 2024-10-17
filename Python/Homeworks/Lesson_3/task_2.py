# Список доступных фильмов
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# Инициализация пустого списка для любимых фильмов
my_list = []

# Ввод количества фильмов, которые пользователь хочет добавить
movies_count = int(input('Сколько фильмов хотите добавить? '))

# Цикл для ввода названий фильмов
for _ in range(movies_count):
    # Ввод названия фильма
    movie = input('Введите название фильма: ')

    # Проверка наличия фильма в списке доступных фильмов
    if movie in films:
        # Добавление фильма в список любимых, если он есть в списке
        my_list.append(movie)
    else:
        # Вывод сообщения об ошибке, если фильма нет в списке
        print(f'Ошибка: фильма {movie} у нас нет :(')
# Вывод списка любимых фильмов
print(f'\nВаш список любимых фильмов: {my_list}')
