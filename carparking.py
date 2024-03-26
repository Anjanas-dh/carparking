from enum import Enum
from dataclasses import dataclass


class Position:
    def __init__(self, floor, spot):
        self.floor = floor
        self.spot = spot


class CarPark:
    def __init__(self, spaces, levels, stairsPosition) -> None:
        self.spaces = spaces
        self.levels = levels
        self.stairsPosition = stairsPosition


@dataclass
class Direction:
    def __init__(self, stepsAmount, walkDirection):
        self.stepsAmount = stepsAmount
        self.walkDirection = walkDirection


class WalkDirection(Enum):
    LEFT = "L"
    RIGHT = "R"
    DOWN = "D"


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

    return get_directions_string(
        [
            Direction(
                stepsAmount=current_position.spot, walkDirection=WalkDirection.RIGHT
            )
        ]
    )


def get_directions_string(directions):
    return " ".join(
        map(
            lambda dir: str(dir.stepsAmount) + dir.walkDirection.value,
            directions,
        )
    )
