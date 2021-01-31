'''Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить
значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях
первого массива стоят четные числа.'''

from random import random
from icecream import ic

size = int(input('Какое кол-во элементов будет в массиве?: '))
array = [int(random() * 100) for el in range(size)]
ic(array)

array_index = []
for num, el in enumerate(array, start=0):
    if el % 2 == 0:
        array_index.append(num)
    ic(num, el)

print(f'Индексы четных элементов: {array_index}')
