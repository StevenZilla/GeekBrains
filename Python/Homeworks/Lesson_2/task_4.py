salary_year = 0
for month in range (1, 13):
    salary_month = int(input(f'Введите зарплату за {month}-ый месяц: '))
    salary_year += salary_month
average_salary = salary_year / 12
print('Средняя зарплата за год:', average_salary)

                    
