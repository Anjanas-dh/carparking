class Position:
    def __init__(self, floor, spot):
        self.floor = floor
        self.spot = spot


def get_car_park_directions(current_position):
    if (
        not isinstance(current_position, Position)
        or not isinstance(current_position.floor, int)
        or not isinstance(current_position.spot, int)
    ):
        return False
    return True
