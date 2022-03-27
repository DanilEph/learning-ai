#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sqr_r(x, y):
    return x ** 2 + y ** 2

def is_in_ring(outer_sqr_r1, inner_sqr_r2, sqr_r_target):
    if inner_sqr_r2 <= sqr_r_target <= outer_sqr_r1:
        return True
    else:
        return False

while(1):
    print ('Определите точку А(x, y): ')
    x = float(input('Введите x = '))
    y = float(input('Введите y = '))
    if (is_in_ring(1, 0.25, sqr_r(x, y))):
        print 'Точка A(' + str(x) + ', ' + str(y) + ') ВХОДИТ в кольцо'
    else:
        print 'Точка A(' + str(x) + ', ' + str(y) + ') НЕ ВХОДИТ в кольцо'
    print('\n')