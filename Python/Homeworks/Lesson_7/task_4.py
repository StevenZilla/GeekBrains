def count_unique_characters(string):
    # Приводим строку к нижнему регистру, чтобы сделать подсчет регистронезависимым
    lower_string = string.lower()
    
    # Используем filter для выбора символов, которые встречаются в строке ровно один раз
    unique_chars = list(filter(lambda c:
 lower_string.count(c.lower()) == 1, lower_string))
 
    # Выводим уникальные символы (по желанию, можно удалить эту строку)
    print(unique_chars)

    # Возвращаем количество уникальных символов
    return len(unique_chars)
 
# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)