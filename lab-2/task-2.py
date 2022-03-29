#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging


def input_two_words(isRepeat = 'repeat'):
    word_1 = raw_input('Введите первое слово: ')
    word_2 = raw_input('Введите второе слов: ')

    if (isRepeat == 'no-repeat' and word_1 == word_2):
        logging.error('Вы ввели два одиноковых слова! Слова не могут быть одинаковыми!')
    else:
        return word_1, word_2

def match_words(word_1, word_2):
    length = 0
    match_count = 0

    if (len(word_1) <= len(word_2)):
        length = len(word_1)
    else:
        length = len(word_2)

    for i in range(length):
        if (word_1[i] == word_2[i]):
            match_count += 1
        else:
            break

    return match_count

variant = input('Слова могут быть одинаковыми? \n(1) да \n(2) нет \n> ')
number_of_letters_in_result = 0

if (variant == 1):
    number_of_letters_in_result = match_words(*input_two_words())
elif (variant == 2):
    number_of_letters_in_result = match_words(*input_two_words('no-repeat'))
else:
    print('Такого пункта нет!')

if (variant == 1 or variant == 2):
    print('Колличество одинаковых начальных букв двух введенных слов равно ' + str(number_of_letters_in_result))