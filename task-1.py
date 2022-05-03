#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def input_array(elem_num: int):
    arr = []
    print('*** ВВОД МАССИВА ***')

    for i in range(elem_num):
        arr.append(float(input(f'Введите элемент {i} массива: ')))

    print('*** Конец ввода массива ***\n')
    return arr


def array_sum(min: float, max: float, arr: []):
    result_arr = list(filter(lambda x: min < x < max, arr))

    return sum(result_arr)


def print_array(arr: []):
    print('*** ВЫВОД МАССИВА ***\n')
    for elem in arr:
        print(elem, '\n')
    print('*** Конец вывода массива ***\n')


print(f'Сумма элементов массива, которые больше 3 и меньше 8, равна:  {array_sum(3, 8, input_array(3))}')
