#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def remove_letters(string):
    filtered_string = filter(str.isdigit, string)
    return filtered_string

sentence = raw_input('Введите предложение: ')
print('Предложение без букв, только цифры: ' + remove_letters(sentence))
