"""Задание 2. Преобразование числа в шестнадцатеричное
представление.
Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте для
проверки своего результата"""


def int_to_hex(n):
    is_negative = n < 0
    n = abs(n)
    if n == 0:
        return '0'

    hex_digits = "0123456789ABCDEF"
    hex_string = ""

    while n > 0:
        remainder = n % 16
        hex_string = hex_digits[remainder] + hex_string
        n //= 16
    if is_negative:
        hex_string = '-' + hex_string

    return hex_string


number = int(input("Введите целое число: "))
hex_representation = int_to_hex(number)
print(f"Шестнадцатеричное представление: {hex_representation}")