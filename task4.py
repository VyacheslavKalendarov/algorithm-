'''По длинам трех отрезков, введенных пользователем, определить возможность существования
треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить,
 является ли он разносторонним, равнобедренным или равносторонним.'''

# https://drive.google.com/file/d/1ggWC41e-FqeFxncLtlWixEbfhvFNgKqF/view?usp=sharing

print("Для определения существования треуголиника и его типа введите длины сторон треугольника")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольника не существует")
elif a != b and a != c and b != c:
    print("Треугольник: разносторонний")
elif a == b == c:
    print("Треугольник: равносторонний")
else:
    print("Треугольник: равнобедренный")