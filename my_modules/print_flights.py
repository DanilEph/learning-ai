def print_flights(arr: []):
    for elem in arr:
        print(f'Название рейса: {elem.get("name")}')
        print(f'Номер рейса: {elem.get("number")}')
        print(f'Пункт назначения: {elem.get("destination")}')
        print(f'Тип самолета: {elem.get("plane_type")}')
        print('--------------')