#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def how_many_cells(cell_numbers_per_division, dividing_period, period):
    all_divisions = period / dividing_period
    return cell_numbers_per_division ** all_divisions

while(1):
    cell_mubers_per_division = input('На сколько клеток делется одна клетка за одно делениие? \n> ')
    dividing_period = input('Какой временной интервал между делениями клеток (в часах)? \n> ')
    period = input('Сколько прошло вренени с момента, когда клетка была одна (в часах)? \n> ')
    print '------------'
    print 'Таким образом, общее количество клеток за равняется ' + str(how_many_cells(cell_mubers_per_division, dividing_period, period))
    print '\n'
