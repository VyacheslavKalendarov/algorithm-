'''В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.'''

from random import random
from icecream import ic

size = int(input('Какое кол-во элементов будет в массиве?: '))
array = [int(random() * 100) for el in range(size)]
ic(array)

if array[0] > array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, size):
    if array[i] < array[min1]:
        b = min1
        min1 = i
        if array[b] < array[min2]:
            min2 = b
    elif array[i] < array[min2]:
        min2 = i

print("№%3d:%3d" % (min1 + 1, array[min1]))
print("№%3d:%3d" % (min2 + 1, array[min2]))

