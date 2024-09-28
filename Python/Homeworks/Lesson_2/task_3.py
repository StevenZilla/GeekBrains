import random

number = random.randint(-100, 100)
print('Загадано число в диапазоне от -100 до 100!')
guess_count = 0
while True:
    guess_num = int(input('Введите число: '))
    guess_count += 1
    if guess_num > number: 
        print('Ваше число больше загаданного!')
    elif guess_num < number:
        print('Ваше число меньше загаданного:')
    else:
        print('Вы угадали! Число попыток:', guess_count)
        break
    