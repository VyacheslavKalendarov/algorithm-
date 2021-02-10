'''По введенным пользователем координатам двух точек вывести уравнение прямой вида
y = kx + b, проходящей через эти точки.'''

# https://drive.google.com/file/d/1ggWC41e-FqeFxncLtlWixEbfhvFNgKqF/view?usp=sharing

print('Введите координаты двух точек:')

x1 = float(input('Введите х1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y2: '))

if x1 == x2:
    print(f'Уравнение прямой, проходящей через точки: x = {x1}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y1 - k * x1
    print(f'Уравнение прямой, проходящей через точки: y = {k}x + {b}')
