#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_asterisks(word):
    number_of_letters = len(word)
    simbol = '*'
    return(simbol * number_of_letters + ' ' + word + ' ' + simbol * number_of_letters)

one_word = raw_input('Введите слово: ')

print(add_asterisks(one_word))

