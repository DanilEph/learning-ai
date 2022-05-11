#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from new_flight import new_flight
from print_flights import print_flights
from flights import get_flight, set_flight

exit = True
while (exit):
    print('\n')
    print('Выберите одну из опций: \n(1) Добавить новый рейс \n(2) Найти рейсы по типу самолета \n(3) Выход')
    user_chose = input('>> ')

    if user_chose == '1':
        set_flight(new_flight())
    elif user_chose == '2':
        print_flights(get_flight(input('\nНайти рейсы по типу самолета >> ')))
    elif user_chose == '3':
        exit = False
    else:
        print('Такой опции нет!')