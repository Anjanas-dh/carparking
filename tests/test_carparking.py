from carparking import Direction, Position, WalkDirection
from carparking import CarPark
from carparking import get_car_park_directions


def describe_carparking():
    def should_return_true_if_position_input_is_all_integers():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=3), CarPark(spaces=1, levels=1, stairsPosition=1)
            )
            != False
        )

    def should_return_false_if_position_floor_property_is_not_an_integer():
        assert (
            get_car_park_directions(
                Position(floor="1", spot=3),
                CarPark(spaces=1, levels=1, stairsPosition=1),
            )
            == False
        )

    def should_return_false_if_position_spot_property_is_not_an_integer():
        assert (
            get_car_park_directions(
                Position(floor=1, spot="3"),
                CarPark(spaces=1, levels=1, stairsPosition=1),
            )
            == False
        )

    def should_return_false_if_input_type_is_not_class_Position():
        assert (
            get_car_park_directions(1, CarPark(spaces=1, levels=1, stairsPosition=1))
            == False
        )

    def should_return_true_if_carpark_input_is_all_integers():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=3),
                CarPark(spaces=15, levels=7, stairsPosition=3),
            )
            != False
        )

    def should_return_false_if_stairs_position_is_not_within_spaces_range():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1),
                CarPark(spaces=10, levels=10, stairsPosition=30),
            )
            == False
        )

    def should_return_false_if_spaces_is_less_than_1():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1),
                CarPark(spaces=-1, levels=1, stairsPosition=1),
            )
            == False
        )

    def levels_shant_be_less_than_1():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1),
                CarPark(spaces=1, levels=-1, stairsPosition=1),
            )
            == False
        )

    def should_return_false_if_stairs_Position_is_less_than_1():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1),
                CarPark(spaces=1, levels=1, stairsPosition=-1),
            )
            == False
        )

    def should_return_directions_1_right_if_carpark_level_is_1_and_position_spot_is_next_to_exit():
        result = get_car_park_directions(
            Position(floor=1, spot=1), CarPark(spaces=1, levels=1, stairsPosition=1)
        )
        testEqual = [Direction(1, WalkDirection.RIGHT)]
        assert result[0].stepsAmount == testEqual[0].stepsAmount
        assert result[0].walkDirection == testEqual[0].walkDirection
        # assert get_car_park_directions(
        #     Position(floor=1, spot=1), CarPark(spaces=1, levels=1, stairsPosition=1)
        # ) is [Direction(1, WalkDirection.RIGHT)]
