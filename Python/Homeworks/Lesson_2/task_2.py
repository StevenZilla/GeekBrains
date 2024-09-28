# Инициализация переменных
hour = 0
summary_tasks = 0
task_per_a_hour = 0
go_to_store = False

print('Начался 8-ми часовой рабочий день')

# Инициализация цикла рабочего дня
while hour != 8:
    hour = hour + 1
    print(hour, 'час')
    task_per_a_hour = int(input('Введите количество задач, котороые Максим решит за этот час: '))
    summary_tasks += task_per_a_hour
    call = int(input('Звонит жена. Взять трубку? 1 - да, 0 - нет: '))
    if call == 1:
        go_to_store = True
    
# Вывод результатов
print('Общее число решенных Максимом задач:', summary_tasks)
if go_to_store == True:
    print('Нужно зайти в магазин')
else: 
    print('В мазаин заходить ненужно')
    