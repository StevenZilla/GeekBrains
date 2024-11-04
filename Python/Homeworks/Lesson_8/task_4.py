# Определяем английский алфавит
english_alphabet='abcdefghijklmnopqrstuvwxyz'
total_letters=0
    
#Открываемфайлtext.txtисчитываемтекст
with open("text.txt", "r") as file:
    text = file.read().lower() # Приводим текст к нижнему регистру
 
 # Создаем словарь для подсче таколичества каждой буквы
 letter_count = {letter: 0 for letter in english_alphabet}

 # Подсчитываем количество вхождений каждой буквы
for char in text:
    if char in english_alphabet:
        letter_count[char]+=1
        total_letters+=1
# Вычисляем частоту встречаемости каждой буквы
letter_freq = {letter: (count / total_letters) for letter,countin letter_count.items()ifcount>0}
 
# Сортируем буквы по убыванию частоты и по алфавиту при равенстве частоты
sorted_letters = sorted(letter_freq.items(),key=lambda x:(-x[1], x[0]))
 
# Записываем результат в файл analysis.txt
with open("analysis.txt", "w") as file:
    for letter, freq in sorted_letters:
        file.write(f"{letter} {freq:.3f}\n")