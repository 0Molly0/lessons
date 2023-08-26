import constants


# def CONSTANTS_VALUES():
#     constants = {
#         'INCHES_IN_METER': 39.370100
#     }
#     return constants


def CONSTANTS_VALUES():
    return {
        'INCHES_IN_METER': 39.370100
    }


def convert_meters_to_inches(meters_co_convert: int | float) -> float:
    """
    according to doc #554 we return only positive values
    https://stackoverflow.com/questions/10116518/im-getting-key-error-in-python
    """
    result = constants.CONSTANTS_METRIC['INCHES_IN_METER'] * meters_co_convert
    # result = CONSTANTS_VALUES()['INCHES_IN_METER'] * meters_co_convert
    abs_result = abs(round(result, 2))
    return abs_result


def calculate_square_area(square_side: int | float) -> float | int:
    # result = square_side ** 2
    result1 = square_side * square_side
    return result1


def check_weather_condition(air_temperature_celsius: int | float) -> str:
    if air_temperature_celsius < 5:
        result = 'hold'
    elif air_temperature_celsius <= 25:
        result = 'norm'
    else:
        result = 'hot'
    return result


def is_cold(air_temperature_celsius) -> bool:
    result = air_temperature_celsius < 5
    return result


def get_rectangle_perimeter(side1: int | float, side2: int | float) -> float:
    if side1 <= 0 or side2 <= 0:
        raise ValueError('Sides cannot be 0 or negative')

    perimeter = (side1 + side2) * 2.0
    return perimeter


get_rectangle_perimeter(0, 6)


def get_cube_volume(side1: int | float, side2: int | float, height: int | float) -> float:
    if height > 10:
        return 0
    volume = side1 * side2 * height
    return volume


# print(get_cube_volume(2, 3, height=4))


def get_cone_volume(height: int | float, diameter: int | float) -> float:
    result = (1 / 3) * 3.1416 * ((diameter / 2) ** 2) * height
    return result


# print(get_cone_volume(diameter=1, height=6))
# print(get_cone_volume(1, 6))
# print(get_cone_volume(2, diameter=6))
