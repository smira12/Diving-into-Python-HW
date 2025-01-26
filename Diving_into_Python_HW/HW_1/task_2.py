"""Задача 2. Треугольник
треугольник существует только тогда, когда сумма любых двух его сторон
больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если
хотя бы в одном случае отрезок окажется больше суммы двух других, то
треугольника с такими сторонами не существует. Отдельно сообщить является
ли треугольник разносторонним, равнобедренным или равносторонним.
"""

a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

if a + b > c and b + c > a and a + c > b:
    print('Треугольник существует!')
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or a == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Такого треугольника не существует')