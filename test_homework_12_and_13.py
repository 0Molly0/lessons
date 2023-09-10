from homework_12_and_13 import sanitize_string
import pytest


def test_sanitize_string():
    base_string = 'nnmmm'
    exclude = 'nmnmghfghh'
    max_len = 5
    expected_result = ['5']
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude
    )
    assert actual_result == expected_result


def test_sanitize_zero_string():
    base_string = ''
    exclude = 'nmnmghfghh'
    max_len = 5
    expected_result = []
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude
    )
    assert actual_result == expected_result


def test_sanitize_overload_string():
    base_string = '11111111111'
    exclude = ['2', 'n']
    max_len = 4
    expected_result = ['1'] * 4
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude,
    )
    assert actual_result == expected_result


def test_sanitize_unsuccess_string():
    base_string = '1' * 500
    exclude = 'nmnmghfghh'
    max_len = 0
    with pytest.raises(ValueError):
        sanitize_string(
            string_value=base_string,
            max_result_length=max_len,
            exclude=exclude,
        )
