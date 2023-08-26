# def get_int_from_user(message: str = 'Enter your age ') -> int:
#     password = 150
#     value = -1
#     while True:
#         value += 1
#         if 10 < value < 20:
#             continue
#
#         print(f'{value=}')
#         if value == password:
#             print(f'{password=}')
#             break
#     return 1


def get_int_from_user(message: str = 'Enter your age (positive integer)') -> float:
    while True:
        user_input = input(message)
        if user_input.replace('.', '', 1).isdigit():
            return float(user_input)
        else:
            print('Your input is not a valid number')


print(get_int_from_user() * 100)
