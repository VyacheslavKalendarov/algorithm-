'''Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.'''


# https://drive.google.com/file/d/14DAUImEa6ksioxo1ndcddTIpv_Sp6ZIr/view?usp=sharing


def proving():
    n = int(input('Введите натуральное число n для равенстава 1+2+...+n = n(n+1)/2: '))
    proof1 = int(n * (n + 1) / 2)
    proof2 = 0
    for i in range(1, n + 1):
        proof2 += i
    if proof1 == proof2:
        return f'''Равенство верное:
        1+2+...+{n} = {n}({n}+1)/2
        {proof1} = {proof2}'''
    else:
        return f'равенство неверное: {proof1} не равно {proof2}'


print(proving())
