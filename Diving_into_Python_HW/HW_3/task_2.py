"""Задача 2. Поиск наибольшего числа в списке
напишите программу, которая принимает список чисел через строку и
возвращает наибольшее число в этом списке.
"""
nums = [int(num) for num in input('Введите числа через пробел: ').split()]

max_number = 0
for number in nums:
    if number > max_number:
        max_number = number

print(nums)
print(max_number)