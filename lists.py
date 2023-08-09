endswith = 'Київ Одеса Львів'.endswith('Львів')
startswith = 'Київ Одеса Львів'.startswith('Київ')

list_of_cities = 'Київ Одеса Львів'.split()
print(list_of_cities)

empty_list1 = []
empty_list2 = list()

list_of_products = [
    'cheese',
    'broccoli',
    'bread',
]

sister_list = [
    'lipstick',
    'chips',
    'beermix',
]

print(id(list_of_products))

first_product = list_of_products[0]
second_product = list_of_products[1]
third_product = list_of_products[2]
# forth_product = list_of_products[3]

for product in list_of_products:
    print(product)
    print(111111)

print(product)

last_product = list_of_products[-1]
two_products = list_of_products[1:]

# detele element
list_of_products.remove('bread')
data = list_of_products.pop(0)
data1 = list_of_products.pop()

# add elements
list_of_products.append('milk')
list_of_products.append('milk2')
list_of_products.insert(0, 'beer')

# for product_from_sister in sister_list:
#     list_of_products.append(product_from_sister)

new_list_purchase = list_of_products + sister_list
new_list_purchase2 = list_of_products[:]
# list_of_products.extend(sister_list)
# list_of_products.extend('ddddddddd')

my_sentence = 'I love food'
last_letter = my_sentence[2:6]

for letter in my_sentence:
    if letter.islower():
        print(letter.upper())
