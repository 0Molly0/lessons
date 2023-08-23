from library import convert_meters_to_inches, calculate_square_area


def test_metr_to_inches_converter_int():
    expected_result = 39.37
    meters = 1
    actual_result = convert_meters_to_inches(meters)
    assert actual_result == expected_result
    assert type(actual_result) == float


def test_meter_to_inches_converter_float():
    expected_result = 61.02
    meters = 1.55
    actual_result = convert_meters_to_inches(meters)
    assert actual_result == expected_result
    assert type(actual_result) == float


def test_square_area():
    side = 2.0
    expected_result = 4
    actual_result = calculate_square_area(side)
    assert actual_result == expected_result
    assert type(actual_result) in {int, float}
