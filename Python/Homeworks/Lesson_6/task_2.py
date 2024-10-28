import random

# Генерация первой команды из 20 случайных вещественных чисел в диапазоне от 5 до 10
first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

# Генерация второй команды аналогично первой
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

# Определение победителей тура путем сравнения значений в первой и второй командах
winners = [
    first_team[i_player] if first_team[i__player] > second_team[i_player]
    else second_team[i_player]
    for i_player in range(20)
]
# Вывод данных
print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', winners)

