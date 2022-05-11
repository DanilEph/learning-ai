#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def new_flight():
    dictionary = {
        'name': input('Введите название рейса: '),
        'number': input('Введите номер рейса: '),
        'destination': input('Введите пункт назначения: '),
        'plane_type': input('Введите тип самолета: '),
    }

    return dictionary
