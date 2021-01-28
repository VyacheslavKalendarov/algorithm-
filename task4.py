'''В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше
или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не
отгадано, то вывести загаданное число.'''

# https://drive.google.com/file/d/14DAUImEa6ksioxo1ndcddTIpv_Sp6ZIr/view?usp=sharing

from random import randint
from icecream import ic

num = randint(0, 100)
ic(num)  # для наглядности загаданного числа при отладке + затестил библиотеку


def guessing_game(num_of_attempts=10):
    print(f'У вас {num_of_attempts} попыток')
    if num_of_attempts == 0:
        return f'Вы проиграли'
    answer = int(input('Введите ваше число от 0 до 100: '))

    if answer == num:
        return f'Поздравляем! Вы угадали'

    elif answer < num and num_of_attempts > 0:
        print(f'Введенное число меньше загадонного, попробуйте еще раз')
        return guessing_game(num_of_attempts - 1)

    elif answer > num and num_of_attempts > 0:
        print(f'Введенное число больше загадонного, попробуйте еще раз')
        return guessing_game(num_of_attempts - 1)

    else:
        return f'Вы проиграли'


print(guessing_game())
