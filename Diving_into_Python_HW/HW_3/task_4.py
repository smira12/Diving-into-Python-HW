"""Задача 4. Генерация паролей
напишите программу, которая генерирует случайный пароль заданной длины,
состоящий из букв, цифр и специальных символов."""

import random
import string

password_len = int(input('Введите длину пароля: '))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(password_len))

print(password)


