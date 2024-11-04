import zipfile

    # Открываем архив и ищем текстовый файл
withzipfile.ZipFile("voina-i-mir.zip", "r") as zip_ref:
    # Получаем список файлов в архиве и выбираем первый текстовый файл
    file_name = [name for name in zip_ref.namelist() if name.endswith('.txt')][0]
    # Открываем выбранный файл и читаем его содержимое
    with zip_ref.open(file_name) as file:
        text = file.read().decode('utf-8')
 
    # Инициализируем словарь для подсчета количества символов
    char_count = {}

# Подсчитываем количество вхождений каждого символа
for char in text:
    if char.isalpha(): # Учитываем только буквы
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
 
 # Сортируем символы по частоте (в убывании) и по алфавиту при равенстве частоты
 sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
 
 # Записываем результаты в файл
 with open("statistik.txt", "w", encoding="utf-8") as file:
    for char, freq in sorted_chars:
        file.write(f"{char}: {freq}\n")