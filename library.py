import constants


# def CONSTANTS_VALUES():
#     constants = {
#         'INCHES_IN_METER': 39.370100
#     }
#     return constants


def CONSTANTS_VALUES():
    return{
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
