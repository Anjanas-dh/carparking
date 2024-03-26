from enum import Enum
from dataclasses import dataclass


class Position:
    def __init__(self, floor, spot):
        self.floor = floor
        self.spot = spot


class CarPark:

    def __init__(self, floors, spots, stairsPosition) -> None:
        self.floors = floors
        self.spots = spots
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


def isInputInvalid(current_position, car_park):
    return (
        not isinstance(current_position, Position)
        or not isinstance(current_position.floor, int)
        or not isinstance(current_position.spot, int)
        or not isinstance(car_park, CarPark)
        or not isinstance(car_park.spots, int)
        or not isinstance(car_park.floors, int)
        or not isinstance(car_park.stairsPosition, int)
        or car_park.stairsPosition > car_park.spots
        or car_park.spots < 1
        or car_park.floors < 1
        or car_park.stairsPosition < 1
    )


def get_car_park_directions(current_position, car_park):

    if isInputInvalid(current_position, car_park):
        return False

    directions = []

    if car_park.floors == 1:
        directions.append(
            Direction(
                stepsAmount=current_position.spot, walkDirection=WalkDirection.RIGHT
            )
        )
    else:
        actualSpot = current_position.spot
        ## directions to the stairs
        diffSpotFromStairPosition = car_park.stairsPosition - current_position.spot
        walkToTheRight = diffSpotFromStairPosition < 0
        stepsToStairs = (
            abs(diffSpotFromStairPosition)
            if walkToTheRight
            else diffSpotFromStairPosition
        )
        directions.append(
            Direction(
                stepsAmount=stepsToStairs,
                walkDirection=(
                    WalkDirection.RIGHT if walkToTheRight else WalkDirection.LEFT
                ),
            )
        )
        ## update the spot you're at
        actualSpot = (
            actualSpot - stepsToStairs if walkToTheRight else actualSpot + stepsToStairs
        )
        ## directions downstairs
        stairsDown = car_park.floors - current_position.floor + 1
        directions.append(
            Direction(stepsAmount=stairsDown, walkDirection=WalkDirection.DOWN)
        )
        ## steps left to the exit
        directions.append(
            Direction(stepsAmount=actualSpot, walkDirection=WalkDirection.RIGHT)
        )

    return get_directions_string(directions)


def get_directions_string(directions):
    return ",".join(
        map(
            lambda dir: str(dir.stepsAmount) + dir.walkDirection.value,
            directions,
        )
    )
