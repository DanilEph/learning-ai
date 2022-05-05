#!/usr/bin/env python3
# -*- coding: utf-8 -*-

flights = []


def new_flight():
    dictionary = {
        'name': input('Введите название рейса: '),
        'number': input('Введите номер рейса: '),
        'destination': input('Введите пункт назначения: '),
        'plane_type': input('Введите тип самолета: '),
    }

    return dictionary


def set_flight(flight: {}):
    flights.append(flight)


def get_flight(plane_type: str):
    arr = list(filter(lambda x: x.get('plane_type') == plane_type, flights))
    return arr


def print_flights(arr: []):
    for elem in arr:
        print(f'Название рейса: {elem.get("name")}')
        print(f'Номер рейса: {elem.get("number")}')
        print(f'Пункт назначения: {elem.get("destination")}')
        print(f'Тип самолета: {elem.get("plane_type")}')
        print('--------------')


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