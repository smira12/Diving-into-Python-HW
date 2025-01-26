"""Задача 4. Яма
Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
Вам поручили создать генератор ландшафта. Напишите программу, которая
получает на вход число N и выводит на экран числа в виде ямы:"""

depth = int(input("Введите глубину ямы: "))

for i in range(depth):
    for left_num in range(depth, depth - i - 1, -1):
        print(left_num, end="")

    point = 2 * (depth - i - 1)
    print("." * point, end="")

    for right_num in range(depth - i, depth + 1):
        print(right_num, end="")

    print()
