'''Посчитать, сколько раз встречается определенная цифра в введенной последовательности
чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются
вводом с клавиатуры.'''

# https://drive.google.com/file/d/14DAUImEa6ksioxo1ndcddTIpv_Sp6ZIr/view?usp=sharing

n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print(f'Было введено {count} цифр {d}')
