def sanitize_string(*, string_value: str, exclude: str | list = 'nN mM', max_result_length: int = 100) -> list[str]:
    if max_result_length < 1:
        raise ValueError('max_result_length cannot be less than 1')

    result_list = []
    if not string_value:
        return result_list

    exclude = set(exclude)
    string_value_length = len(string_value)
    position = 0

    while position < string_value_length:
        if string_value[position] not in exclude:
            result_list.append(string_value[position])
            if len(result_list) == max_result_length:
                break
        position += 1
    return result_list


def humanize_car_trip_info(*, seconds: int, speed_meters_per_seconds: int | float, car_weight: int) -> str:
    MIN_ALLOWED_VALUE = 0
    if seconds < MIN_ALLOWED_VALUE:
        raise ValueError(f'seconds value cannot be less than {MIN_ALLOWED_VALUE}')
    if speed_meters_per_seconds < MIN_ALLOWED_VALUE:
        raise ValueError(f'speed_meters_per_seconds value cannot be less than {MIN_ALLOWED_VALUE}')
    if car_weight < MIN_ALLOWED_VALUE:
        raise ValueError(f'car_weight value cannot be less than {MIN_ALLOWED_VALUE}')

    result = f"Транспортний засіб вагою {car_weight} кг рухався {seconds} секунд зі швидкістю {speed_meters_per_seconds}" \
             f" м/сек, і подолав відстань {seconds * speed_meters_per_seconds} метрів"
    return result
