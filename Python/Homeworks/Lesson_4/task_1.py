# Даны три списка
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Задача 1: найти элементы, которые есть в каждом списке

# Решение без использования множеств
all_elems = array_1 + array_2 + array_3 # Объединяем все списки в один
new_elems_1 = []
for elem in all_elems:
    # Проверяем, если элемент не добавлен ранее и присутствует во всех трех списках
    if elem not in new_elems_1 and all(elem in array for array in [array_1, array_2, array_3]):
        new_elems_1.append(elem) # Добавляем элемент в результат
print("Решение без множеств:", new_elems_1)

# Решение с использованием множеств
new_elems_1_set = set(array_1) & set(array_2) & set(array_3) # Пересечение трех множеств

print("Решение с множествами:", new_elems_1_set)

# Задача 2: найти элементы из первого списка, которых нет во втором и третьем списках
# Решение без использования множеств
new_elems_2 = []
for elem in array_1:
    # Проверяем, если элемент отсутствует во втором и третьем списках
    if elem not in array_2 and elem not in array_3:
        new_elems_2.append(elem) # Добавляем элемент в результат
print("Решение без множеств:", new_elems_2)

# Решение с использованием множеств
new_elems_2_set = set(array_1) - set(array_2) - set(array_3) #Разность множеств
print("Решение с множествами:", new_elems_2_set)