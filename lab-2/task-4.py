#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def match_words(word_1, word_2):
    for letter_of_word_1 in word_1:
        middle_letter = 'нет'
        for letter_of_word_2 in word_2:
            if (letter_of_word_1 == letter_of_word_2):
                middle_letter = 'да'
                break
        print(middle_letter)

word_1 = raw_input('Введите первое слово: ')
word_2 = raw_input('Введите второе слово: ')

match_words(word_1, word_2)
