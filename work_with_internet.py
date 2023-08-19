from pprint import pprint

import requests

# url = 'https://helix.ru/kb/item/18-023'
# url = 'https://dummyjson.com/products?limit=10&skip=10'
url = 'https://dummyjson.com/products'

params = {
    'limit': 100,
    'skip': 0,
}

response = requests.get(url=url, params=params)

# print(response.status_code)
# print(response.content)
# print(response.text)
result = response.json()
products = result['products']
# total = result['total']
# total = len(result['products'])
# pprint(products)

total_cost = 0
total_cost_apple = 0
total_cost_premium = 0

for product in products:
    # print(product)
    price = product['price']
    stock = product['stock']
    product_cost = price * stock
    total_cost += product_cost

    if product['brand'].title().strip() == 'Apple':
        total_cost_apple += product_cost

    if price > 400:
        total_cost_premium += product_cost

print(f'{total_cost=}')
print(f'{total_cost_apple=}')
print(f'{total_cost_premium=}')
