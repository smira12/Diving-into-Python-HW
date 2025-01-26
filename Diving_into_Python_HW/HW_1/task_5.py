"""Задача 5. Игра «Компьютер угадывает число»
Мальчик загадывает число между 1 и 100 (включительно). Компьютер может
спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из
трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
Напишите программу, которая с помощью цепочки таких вопросов и ответов
мальчика угадывает число.
Дополнительно: сделайте так, чтобы можно было гарантированно угадать
число за семь попыток.
"""

start = 1
finish = 100

count = 1

while True:
    n = (start + finish) // 2
    print('Загаданное число равно, меньше или больше', n)

    answer = int(input('1 - равно, 2 - меньше, 3 - больше?: '))
    if answer == 1:
        print(f'Я угадал! Ура! с', {count}, 'попытки')
        break
    elif answer == 2:
        finish = n
    elif answer == 3:
        start = n
    count += 1