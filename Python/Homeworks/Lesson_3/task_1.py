# Ввод количества видеокарт
videoСardsNumber = int(input('Введите количество видеокарт: '))

# Инициализация списка для хранения видеокарт
videoСards = []
newVideoCardsList = []
maxItem = 0

# Заполнение списка видеокарт и определение наибольшего элемента
for item in range(videoСardsNumber):
	# Ввод номера видеокарты и добавление в список
	videoСards.append(int(input(f'Видеокарта {item + 1}: ')))

	# Обновление значения максимального элемента
	if videoСards[item] > maxItem:
		maxItem = videoСards[item]

# Формирование нового списка без наибольших элементов
for item in range(videoСardsNumber):
	if videoСards[item] != maxItem:
		newVideoCardsList.append(videoСards[item])
# Вывод старого списка видеокарт
print()
print('Старый список видеокарт: [', end=' ')
for item in range(videoСardsNumber):
	print(videoСards[item], end=' ')
print(']')

# Вывод нового списка видеокарт
print('Новый список видеокарт: [', end=' ')
for item in range(len(newVideoCardsList)):
	print(newVideoCardsList[item], end=' ')
print(']')