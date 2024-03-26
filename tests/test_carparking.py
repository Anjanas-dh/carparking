from carparking import Direction, Position, WalkDirection
from carparking import CarPark
from carparking import get_car_park_directions


def describe_carparking():
    def should_return_true_if_position_input_is_all_integers():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=3), CarPark(floors=1, spots=1, stairsPosition=1)
            )
            != False
        )

    def should_return_false_if_position_floor_property_is_not_an_integer():
        assert (
            get_car_park_directions(
                Position(floor="1", spot=3),
                CarPark(floors=1, spots=1, stairsPosition=1),
            )
            == False
        )

    def should_return_false_if_position_spot_property_is_not_an_integer():
        assert (
            get_car_park_directions(
                Position(floor=1, spot="3"),
                CarPark(floors=1, spots=1, stairsPosition=1),
            )
            == False
        )

    def should_return_false_if_input_type_is_not_class_Position():
        assert (
            get_car_park_directions(1, CarPark(floors=1, spots=1, stairsPosition=1))
            == False
        )

    def should_return_true_if_carpark_input_is_all_integers():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=3),
                CarPark(floors=7, spots=15, stairsPosition=3),
            )
            != False
        )

    def should_return_false_if_stairs_position_is_not_within_spots_range():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1),
                CarPark(floors=10, spots=10, stairsPosition=30),
            )
            == False
        )

    def should_return_false_if_spots_is_less_than_1():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1),
                CarPark(floors=1, spots=-1, stairsPosition=1),
            )
            == False
        )

    def floors_shant_be_less_than_1():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1),
                CarPark(floors=-1, spots=1, stairsPosition=1),
            )
            == False
        )

    def should_return_false_if_stairs_Position_is_less_than_1():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1),
                CarPark(floors=1, spots=1, stairsPosition=-1),
            )
            == False
        )

    def should_return_directions_1_right_if_carpark_level_is_1_and_position_spot_is_next_to_exit():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=1), CarPark(floors=1, spots=1, stairsPosition=1)
            )
            == "1R"
        )

    def should_return_directions_2_right_if_carpark_level_is_1_and_position_spot_is_2_away_from_exit():
        assert (
            get_car_park_directions(
                Position(floor=1, spot=2), CarPark(floors=1, spots=2, stairsPosition=1)
            )
            == "2R"
        )

    def should_return_directions_right_if_carpark_level_is_2_and_position_spot_is_next_to_exit():
        assert (
            get_car_park_directions(
                Position(floor=2, spot=1),
                CarPark(floors=2, spots=10, stairsPosition=4),
            )
            == "3L,1D,4R"
        )


## | 10 | 9 | 8 | 7 | 6 | 5 | ST | 3 | 2 | 1* |
## | 10 | 9 | 8 | 7 | 6 | 5 | ST | 3 | 2 | 1 | Exit
