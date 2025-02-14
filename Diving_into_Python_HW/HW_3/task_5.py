"""Задача 5. Нахождение анаграмм
напишите программу, которая принимает два слова и определяет, являются ли
они анаграммами."""

# from collections import Counter
#
# def anagrams_counter(str1, str2):
#     str1 = str1.lower().replace(' ', '')
#     str2 = str2.lower().replace(' ', '')
#     return Counter(str1) == Counter(str2)
#
#
# word1 = input('Введите первое слово: ')
# word2 = input('Введите второе слово: ')
#
# print(anagrams_counter(word1, word2))

word_1 = input('Введите первое слово: ').lower()#.replace(' ', '')
word_2 = input('Введите второе слово: ').lower()#.replace(' ', '')

if len(word_1) != len(word_2):
    print('Слова не являются анаграммами!')
else:
    char_count1 = {}
    char_count2 = {}
    for char in word_1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1
    for char in word_2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    if char_count1 == char_count2:
        print('Слова являются анаграммами')
    else:
        print('Слова не являются анаграммами')


