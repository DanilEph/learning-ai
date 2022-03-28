#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from scipy import integrate

def function(t):
    return math.cos((math.pi / 2) * (t ** 2))

x = input('Введите x: ')
v, err = integrate.quad(function, 0, x)
print 'Ответ: ' + str(v)