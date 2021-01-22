'''1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.'''
# https://drive.google.com/file/d/1ggWC41e-FqeFxncLtlWixEbfhvFNgKqF/view?usp=sharing

a = int(input('Введите трехзначное число: '))

num1 = a // 100
num2 = (a // 10) % 10
num3 = a % 10

print(f'Сумма цифр трехзначного числа: {num1 + num2 + num3}')
print(f'Произведение цифр трехзначного числа: {num1 * num2 * num3}')