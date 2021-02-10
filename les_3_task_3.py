'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

from random import random
from icecream import ic

size = int(input('Какое кол-во элементов будет в массиве?: '))
array = [int(random() * 100) for el in range(size)]
ic(array)

min_ = 0
max_ = 0
for i, el in enumerate(array, start=0):
    if array[i] < array[min_]:
        min_ = i
    elif array[i] > array[max_]:
        max_ = i

ic(array[min_], array[max_])
array[min_], array[max_] = array[max_], array[min_]
print(array)
