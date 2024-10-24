def flatten(a_list):
    # Инициализация пустого списка для хранения результата
    result = []
    
    # Перебор каждого элемента в списке
    for e in a_list:
        # Проверка, является ли элемент целым числом
        if isinstance(e, int):
            result.append(e) # Добавление числа в результат
        else:
            # Рекурсивный вызов функции для вложенного списка
            result.extend(flatten(e)) # Раскрытие вложенных списков
    # Возвращаем окончательный результат
    return result

# Исходный список с вложенными элементами
nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

# Применение функции для получения списка с раскрытыми элементами
flattened_list = flatten(nice_list)

# Вывод результата
print(flattened_list) # Ожидаемый результат: [1, 2, 3