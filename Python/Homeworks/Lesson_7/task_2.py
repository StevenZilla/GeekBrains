from typing import List, Tuple

# Исходные списки
strings = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Создание списка кортежей, состоящих из пар элементов из обоих списков
results: List[Tuple[str, int]] = list(map(lambda x, y: (x, y), strings, numbers))

# Вывод результатов 
print(results)