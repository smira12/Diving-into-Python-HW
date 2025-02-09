from fractions import Fraction

"""Задача 4. Сумма и произведение дробей
Программа принимает две строки вида "a/b" - дробь с числителем и
знаменателем. Возвращает сумму и произведение дробей. Для проверки
используется модуль fractions.
"""

frac1 = input('Введите первую дробь (a/b): ')
frac2 = input('Введите вторую дробь (a/b): ')

numerator1, denominator1 = map(int, frac1.split('/'))
numerator2, denominator2 = map(int, frac2.split('/'))

f1 = Fraction(numerator1, denominator1)
f2 = Fraction(numerator2, denominator2)

sum_frac = f1 + f2
product_frac = f1 * f2

print("Сумма:", sum_frac)
print("Произведение:", product_frac)
