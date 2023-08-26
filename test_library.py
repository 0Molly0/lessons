from random import randint

import pytest

from library import convert_meters_to_inches, calculate_square_area, check_weather_condition, is_cold


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


weather = [
    (randint(-240, 4), 'hold'),
    (randint(5, 25), 'norm'),
    (randint(26, 1000), 'hot'),
]


@pytest.mark.parametrize('temp, expected', weather)
def test_check_weather_condition_cold(temp, expected):
    actual = check_weather_condition(temp)
    assert actual == expected


cold = [
    (randint(-240, 4), True),
    (randint(5, 1000), False),
]


@pytest.mark.parametrize('temp, expected', cold)
def test_is_cold(temp, expected):
    assert is_cold(temp) is expected
