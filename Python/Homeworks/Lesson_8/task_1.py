import os

# Открываем входной файл для чтения
numbers_file=open("numbers.txt","r",encoding="utf-8")

# Инициализируем переменную для хранения суммыч исел
total_sum=0

# Читаем файл построчно
for line in numbers_file:

    # Разбиваем строку на части, используя пробелы и новые строки в качестве разделителей
    # Преобразуем каждую часть в целое число и накапливаем сумму
    numbers=[int(num)fornuminline.split()ifnum]
    total_sum+=sum(numbers)
 
# Закрываем файл после чтения
numbers_file.close()

# Открываем выходной файл для записи
sum_file=open("answer.txt","w",encoding="utf-8")

# Записываем сумму в выходной файл
sum_file.write(str(total_sum))

# Закрываем выходной файл
sum_file.close()