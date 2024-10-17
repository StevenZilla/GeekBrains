# Исходный список чисел
original_list = [1, 4, -3, 0, 10]

# Вывод исходного списка
print('Изначальный список: ', original_list)

# Реализация сортировки пузырьком (Bubble Sort)
for i in range(len(original_list) - 1):
    # Проход по всем элементам списка, за исключением уже отсортированных
    for j in range(len(original_list) - 1 - i):
        # Сравнение текущего элемента с следующим
        if original_list[j] > original_list[j + 1]:
            # Если текущий элемент больше следующего, меняем их местами
            original_list[j], original_list[j + 1] = original_list[j+ 1], original_list[j]
# Вывод отсортированного списка
print('Отсортированный список: ', original_list)
