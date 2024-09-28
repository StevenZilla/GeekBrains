# Запрос данных
num = int(input('Введите шестизначное число: '))
if len(str(num)) == 6:
    # Деление числа на единицы
    num_1 = num // 100000
    num_2 = (num % 100000) // 10000
    num_3 = (num % 10000) // 1000
    num_4 = (num % 1000) // 100
    num_5 = (num % 100) // 10
    num_6 = num % 10
    
    # Определение "счастливого билета"
    if (num_1 + num_2 + num_3) == (num_4 + num_5 + num_6):
        print('Ваш билет счастливый!')
    else: 
        print('Ваш билет не является счастливым.')
else: 
    print('Вы ввели не шестизначное число!')