# Определить, является ли год, который ввел пользователем, високосным или не високосным.

# https://drive.google.com/file/d/1ggWC41e-FqeFxncLtlWixEbfhvFNgKqF/view?usp=sharing

y = int(input())

if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print("Обычный")
else:
    print("Високосный")
