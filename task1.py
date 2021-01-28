'''Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна
завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный
знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать
знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в
качестве делителя.
'''


# https://drive.google.com/file/d/14DAUImEa6ksioxo1ndcddTIpv_Sp6ZIr/view?usp=sharing

def calculate():
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    operation = input('''Введите математическую операцию, которую хотите выполнить:
+ для сложения
- для вычитания
* для умножения
/ для деления
0 завершение программы
''')

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        return calculate()


    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        return calculate()


    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        return calculate()

    elif operation == '/' and number_2 == 0:  # отработка деления на ноль
        print('На ноль делить нельзя, попробуйте заново')
        return calculate()

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        return calculate()


    elif operation == '0':
        return f'программа завершена'

    else:
        print('Вы ввели неправильную операцию, запустите программу еще раз.')
        return calculate()


print(calculate())
