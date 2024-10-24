# Функция для поиска ключа в словаре с учётом глубины поиска
def find_key(struct, key, max_depth=None, depth=1):
    result = None # Переменная для хранения найденного значения

    # Если указана максимальная глубина и текущая глубина превышает её, прекращаем поиск
    if max_depth and max_depth < depth:
        return result
    # Если ключ найден в текущем уровне словаря, возвращаем его значение
    if key in struct:
        return struct[key]
    
    # Рекурсивный поиск по вложенным словарям
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, max_depth, depth=depth + 1)
        if result:
            break

    return result

# Пример словаря с вложенными структурами
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

while True:
    key = input('Введите искомый ключ: ') # Запрашиваем ключ у пользователя
    answer = input('Хотите ввести максимальную глубину? Y/N: ') #Проверяем, хочет ли пользователь ограничить глубину поиска
    if answer.lower() == 'y':
        max_depth = int(input('Введите максимальную глубину: ')) #Если да, запрашиваем максимальную глубину
    else:
        max_depth = None # Если нет, устанавливаем максимальную глубину как None
    
    # Выводим найденное значение ключа или None, если ключ не найден
    print('Значение ключа:', find_key(struct=site, max_depth=max_depth, key=key))