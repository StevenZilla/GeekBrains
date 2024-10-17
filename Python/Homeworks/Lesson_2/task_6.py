boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))

answer = ''
if (boys > girls * 2) or (girls > boys * 2):
    print('Нет решения')
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += 'BGB'
        for bg in range(girls - k):
            answer += 'GB'
else:
     k = girls - boys
     for gbg in range(k):
        answer += 'GBG'
        for gb in range(boys - k):
            answer += 'BG'
            
print(answer)
