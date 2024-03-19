from carparking import Position
from carparking import CarPark
from carparking import get_car_park_directions


def describe_carparking():
    def should_return_true_if_position_input_is_all_integers():
        assert get_car_park_directions(Position(1, 3), CarPark(1, 1, 1)) == True

    def should_return_false_if_position_floor_property_is_not_an_integer():
        assert get_car_park_directions(Position("1", 3), CarPark(1, 1, 1)) == False

    def should_return_false_if_position_spot_property_is_not_an_integer():
        assert get_car_park_directions(Position(1, "3"), CarPark(1, 1, 1)) == False

    def should_return_false_if_input_type_is_not_class_Position():
        assert get_car_park_directions(1, CarPark(1, 1, 1)) == False

    def should_return_true_if_carpark_input_is_all_integers():
        assert get_car_park_directions(Position(1, 3), CarPark(15, 7, 3)) == True

    def should_return_false_if_stairs_position_is_not_within_spaces_range():
        assert (
            get_car_park_directions(
                Position(1, 1), CarPark(spaces=10, levels=10, stairsPosition=30)
            )
            == False
        )
