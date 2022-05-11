flights = []

def set_flight(flight: {}):
    flights.append(flight)


def get_flight(plane_type: str):
    arr = list(filter(lambda x: x.get('plane_type') == plane_type, flights))
    return arr