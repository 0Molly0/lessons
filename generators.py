# data = [5, 8, 9]
# set_data = {item for item in data}
# print(set_data)
#
# list_data = {item * 2 for item in data}
# print(list_data)
#
# dict_data = {item: item for item in data}
# print(dict_data)
#
# generator_data = (item for item in data)
# print(generator_data)
#
# print(next(generator_data))
# print(next(generator_data))
# data[2] = 200
# print(next(generator_data))


def our_generator():
    yield 5
    yield 6
    yield 100


generator_obj = our_generator()
print(next(generator_obj))
print(next(generator_obj))
print(next(generator_obj))
