#Открываемфайлfirst_tour.txtдлячтения
with open("first_tour.txt", "r")as file:
    lines = file.readlines()
    # Первая строка содержит число K
    K = int(lines[0])
    # Словарь для хранения данных участников
    participants = {}
    # Словарь для хранения участников, прошедших во второй тур
    filter_player = {}
    count = 1
    
# Обрабатываем оставшиеся строки
for line in lines[1:]:
    # Разделяем строку на части
    data = line.strip().split()
    # Формируем имя участника с инициалом
    name = f"{data[1][0]}.{data[0]}"
    # Получаем количество баллов
    score=int(data[-1])
    # Сохраняем участника и его баллы
    participants[name]=score

# Фильтруем участников, набравших более K баллов
for player ,score in participants.items():
    if score > K:
        filter_player[player] = score

# Сортируем участников по убыванию баллов
sorted_filter_player = dict(sorted(filter_player.items(), key=lambda x: x[1], reverse=True))
# Открываем файл second_tour.txt для записи
with open("second_tour.txt", "w") as file:
    # Записываем количество участников второго тура
    file.write(f"{len(sorted_filter_player)}\n")
    # Записываем данные участников с нумерацией
    for player, score in sorted_filter_player.items():
        file.write(f"{count}) {player} {score}\n")
        count += 1