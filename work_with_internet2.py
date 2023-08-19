from pprint import pprint

import requests

url = 'https://dummyjson.com/users'

params = {
    # 'limit': 100,
    # 'skip': 0,
}

response = requests.get(url=url, params=params)
result = response.json()
# pprint(result)

users = result['users']
# pprint(users)

city = 'Louisville'
list_of_louisville_users = []

for user in users:
    # pprint(user)
    user_address = user['address']
    user_city = user_address.get('city', '')
    if user_city.title() == city:
        list_of_louisville_users.append(f'{user["firstName"]} {user["lastName"]}')

pprint(list_of_louisville_users)
