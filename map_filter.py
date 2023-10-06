our_list = [5, '8', 18] * 100
#
# res_list = []
# for item in our_list:
#     print(item * 3)
#     res_list.append(item * 3)
#
# print(res_list)


def mult_3(item):
    return item * 3


# another_list = map(lambda item: item * 3, our_list)
another_list = map(mult_3, our_list)
# print(list(another_list))
# print(type(another_list))
# print(next(another_list))

# for i in another_list:
#     print(i)

list_2 = [1, 2, 3, 4, 5] * 2
another_list_2 = map(lambda item: item * 10, list_2)

# print(next(another_list_2))
# print(next(another_list_2))
# list_2[2] = 200
# print(next(another_list_2))
# print(next(another_list_2))


def more3(item):
    return item > 3


# clean_data = filter(lambda item: item > 3, list_2)
clean_data = filter(more3, list_2)
# print(list(clean_data))
# list_2[2] = 200
# print(next(clean_data))
# print(next(clean_data))
# print(next(clean_data))
# print(next(clean_data))

super_data = map(mult_3, filter(more3, list_2))
print(list(super_data))



