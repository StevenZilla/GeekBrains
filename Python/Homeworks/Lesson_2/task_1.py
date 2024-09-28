# Инициализация счетчиков
positive_count = 0
negative_count = 0

# Введение первого значения и начало цикла подсчета
rating = int(input('Введите значение от -100 до 100: '))
while rating != 0:
    if rating > 0:
        positive_count = positive_count + 1
    else: 
        negative_count = negative_count + 1
    rating = int(input('Введите значение от -100 до 100: '))
    
# Вывод количества отзывов
print('Количество положительных отзывов:', positive_count)
print('Количество негативных отзывов:', negative_count)

