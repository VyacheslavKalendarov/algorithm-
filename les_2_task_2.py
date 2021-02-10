'''Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено
число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''


# https://drive.google.com/file/d/14DAUImEa6ksioxo1ndcddTIpv_Sp6ZIr/view?usp=sharing

def counter():
    num = int(input('Введите ваше натуральное число: '))
    even = odd = 0
    while num >= 1:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10  # отбрасываем последнюю цифру, оставляя целую часть
    return f'четных знаков: {even} \nнечетных знаков: {odd}'


print(counter())
