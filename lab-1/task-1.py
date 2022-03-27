#!/usr/bin/env python3
# -*- coding: utf-8 -*-

listOfMonths = [
    'Декабрь',
    'Январь',
    'Февраль',
    'Март',
    'Апраль',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
]

def getMonthOfSeason(numberOfSeason) :
    monthOfSeason = []
    x = 0
    for i in range(0, 4):
        if (i + 1 == numberOfSeason):
            for j in range(0+3*i, 3+3*i):
                monthOfSeason.append(listOfMonths[j])
            break
    return  monthOfSeason


while(1):
    m = int(input('Выберите время года (введите соответствующую цифру): \n(1) Зима \n(2) Весна \n(3) Лето \n(4) Осень \n> '))

    if (m == 1):
        print 'Зима имеет следующие месяцы: ' + ", ".join(getMonthOfSeason(m))
    elif (m == 2):
        print 'Весна имеет следующие месяцы: ' + ", ".join(getMonthOfSeason(m))
    elif (m == 3):
        print 'Лето имеет следующие месяцы: ' + ", ".join(getMonthOfSeason(m))
    elif (m == 4):
        print 'Осень имеет следующие месяцы: ' + ", ".join(getMonthOfSeason(m))
    else:
        print 'Такого времени года нет!'

    print '\n'