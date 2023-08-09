some_list = [565665, ',ggkgbgvv', 5656, '', [], [56, 56], 2.5, True]

correct_list_with_numbers = []

for element in some_list:
    valid_types = [int, float]

    # if type(element) == int or type(element) == float:
    if type(element) in valid_types:
        correct_list_with_numbers.append(element)

print(correct_list_with_numbers)

summa = 0

for number in correct_list_with_numbers:
    summa += number

print(summa)
