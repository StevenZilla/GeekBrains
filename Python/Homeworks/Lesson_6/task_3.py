# Создание двумерного списка с помощью list comprehension
# Внешний цикл по range(1, 5) определяет первый элемент каждой вложенной строки
# Внутренний цикл формирует элементы каждой строки с шагом 4
my_list = [[j_num for j_num in range(i_list, 13, 4)] for i_list in range(1, 5)]
print(my_list)
# Альтернативный вариант решения с использованием фиксированных смещений
second_answer = [[value, value + 4, value + 8] for value in range(1,5)]
print(second_answer)