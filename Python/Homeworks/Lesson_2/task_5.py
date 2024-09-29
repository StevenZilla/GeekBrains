total_cards = int(input('Введите общее число карт: '))
total_sum = 0
for card in range(1, total_cards + 1):
    total_sum += card

for card in range(total_cards - 1):
    remaining_card = int(input('Номер оставшейся карты: '))
    total_sum -= remaining_card  
    
print('Номер потерявшейся карты:', total_sum)