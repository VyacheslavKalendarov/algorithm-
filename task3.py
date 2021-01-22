# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# https://drive.google.com/file/d/1ggWC41e-FqeFxncLtlWixEbfhvFNgKqF/view?usp=sharing

print('Введите три разных числа')
a = float(input('Введите 1е число: '))
b = float(input('Введите 2е число: '))
c = float(input('Введите 3е число: '))

if a > b > c or c > b > a:
    print(f'Среднее число: {b=}')
elif a > c > b or b > c > a:
    print(f'Среднее число: {c=}')
else:
    print(f'Среднее число: {a=}')
