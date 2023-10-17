from pprint import pprint

import certifi
import pymongo
from config_my import USER, PASSWORD
# from bson import Decimal128

url = f'mongodb+srv://{USER}:{PASSWORD}@cluster0.gtwu5zq.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url, tlsCAFile=certifi.where())

db = client.testDB
collection_products = db.products


# products = [
#     {
#         'title': 'bread',
#         'price': 45,
#         'remains': 10,
#         'comment': 'no sugar',
#         'contain_gluten': True,
#     },
#     {
#         'title': 'soft drink',
#         'price': 25,
#         'remains': 100,
#         'comment': 'no sugar',
#         'contain_gluten': False,
#     },
#     {
#         'title': 'milk',
#         'price': 15,
#         'remains': 1,
#         'comment': 'no sugar',
#         'contain_gluten': True,
#     },
#     {
#         'title': 'vinegar',
#         'price': 25,
#         'remains': 10,
#         'comment': 'no sugar',
#         'contain_gluten': False,
#     },
# ]

# collection_products.insert_many(products)

# analog find
# query = []
# response = collection_products.aggregate(query)
# for doc in response:
#     print(doc)
# print(list(response))


# $match stage

# query = [{'$match': {'contain_gluten': False}}]
# response = collection_products.aggregate(query)
# print(list(response))


# query = [{'$match': {'$and': [  # $or
#     {'contain_gluten': False},
#     {'price': {'$gte': 20}}
# ]}}]
# response = collection_products.aggregate(query)
# print(list(response))


# # $group stage
# query = [
#     {
#         '#group': {'_id': '$contain_gluten'}
#     }
# ]
#
# response = collection_products.aggregate(query)
# print(list(response))


# query = [
#     {
#         '$group': {'_id': {'gluten': '$contain_gluten', 'price': '$price'}}
#     }
# ]
#
# response = collection_products.aggregate(query)
# print(list(response))


# $sum stage
# query = [
#     {
#         '$group': {'_id': {'gluten': '$contain_gluten', 'count': {'$sum': '$remains'}}}
#     }
# ]
# response = collection_products.aggregate(query)
# print(list(response))

# query = [
#     {
#         '$group': {'_id': {'gluten': '$contain_gluten', 'count': {'$sum': '$remains'}}}
#     }
# ]
# response = collection_products.aggregate(query)
# print(list(response))


# query = [
#     {
#         '$group': {
#             '_id': '$contain_gluten',
#             'count_remains': {'$sum': '$remains'},
#             'naming_counter': {'$sum': 1}
#                     }
#     }
# ]
# response = collection_products.aggregate(query)
# pprint(list(response))

# $project stage
# query = [
#     {
#         '$project': {
#             '_id': 0,
#             'contain_gluten': 1,
#             'item_description': {'$concat': ['$title', ' - ', '$comment']},
#
#                     }
#     }
# ]
# response = collection_products.aggregate(query)
# pprint(list(response))


# COOL AGGREGATION

my_query = [
    {'$match': {'price': {'$gt': 25}}},
    {'$project': {
        'contain_gluten': 1,
        '_id': 0,
        'this_product_cost': {'$multiply': ['$price', '$remains']}},
     },

    {'$group': {
        '_id': '$contain_gluten',
        'total': {'$sum': '$this_product_cost'},
    }},
    {'$match': {'total': {'$gt': 50}}},
]

response = collection_products.aggregate(my_query)
pprint(list(response))
