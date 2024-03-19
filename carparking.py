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
        or car_park.stairsPosition > car_park.spaces
        or car_park.spaces < 1
        or car_park.levels < 1
        or car_park.stairsPosition < 1
    ):
        return False
    return True
