'''Пользователь вводит данные о количестве предприятий, их наименования и прибыль
 за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить
 среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
 чья прибыль выше среднего и ниже среднего.
'''

from collections import defaultdict

a = defaultdict(int)

company = int(input('Введите количество компаний: '))

for i in range(company):
    name_company = input(f'Введите название {i + 1}й компаний: ')
    for j in range(4):
        income = int(input(f'Прибыль за {j + 1}й квартал: '))
        a[name_company] += income
print(a)

avg_income = sum(a.values()) / company
print(f'Средняя прибыль для всех придприятий за год, составит:\n {avg_income:.3f}')

print(f'Предприятия, где прибыль больше средней:')
for key, value in a.items():
    if value > avg_income:
        print(key)

print(f'Предприятия, где прибыль меньше средней: {key}')
for key, value in a.items():
    if value < avg_income:
        print(key)

