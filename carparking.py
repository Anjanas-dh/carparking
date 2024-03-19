class Position:
    def __init__(self, floor, spot):
        self.floor = floor
        self.spot = spot


class CarPark:
    def __init__(self, spaces, levels, stairsPosition) -> None:
        self.spaces = spaces
        self.levels = levels
        self.stairsPosition = stairsPosition


def get_car_park_directions(current_position, car_park):
    if (
        not isinstance(current_position, Position)
        or not isinstance(current_position.floor, int)
        or not isinstance(current_position.spot, int)
        or not isinstance(car_park, CarPark)
        or not isinstance(car_park.spaces, int)
        or not isinstance(car_park.levels, int)
        or not isinstance(car_park.stairsPosition, int)
    ):
        return False
    return True
