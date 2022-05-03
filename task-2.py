#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def input_array(elem_num: int):
    arr = []
    print('*** ВВОД МАССИВА ***')

    for i in range(elem_num):
        arr.append(float(input(f'Введите элемент {i} массива: ')))

    print('*** Конец ввода массива ***\n')
    return arr


def print_array(arr: []):
    print('*** ВЫВОД МАССИВА ***\n')
    for elem in arr:
        print(elem, '\n')
    print('*** Конец вывода массива ***\n')


def sum_before(arr: [float]):
    sum: float = 0
    last_elem_i: float

    for i, elem in enumerate(arr):
        if elem >= 0:
            last_elem_i = i

    for i, elem in enumerate(arr):
        if i == last_elem_i:
            break
        sum += elem

    return sum


def compress_arr(a: float, b: float, init_arr: []):
    for i, elem in enumerate(init_arr):
        if a <= math.fabs(elem) <= b:
            init_arr[i] = 0
    init_arr.sort(reverse=True)
    return init_arr


arr = input_array(4)

print('1. Максимальный элемент списка: ')
print(max(arr), '\n')

print('2. Cумма элементов списка, расположенных до последнего положительного элемента: ')
print(sum_before(arr), '\n')

print('3. Сжать список, удалив из него все элементы, модуль которых находится в интервале [а, b]. Освободившиеся в конце списка элементы заполнить нулями: ')
print(compress_arr(3, 5, arr))
