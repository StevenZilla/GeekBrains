# Запрашиваем у пользователя ввод текста
text = input('Введите текст: ')
# Создаём список гласных букв, которые есть в тексте

# Используем генератор списка для фильтрации гласных
vowels = [i for i in text if i in 'ауоыиэяюёе']

# Выводим список найденных гласных
print('Список гласных букв:', vowels)

# Выводим количество гласных в списке
print('Длина списка:', len(vowels))
