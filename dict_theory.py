# dick
# словник - це структура данихб яка складається з незмінного ключа та будь-якого значення
# значенням може бути інший словник
# словники бажано створювати для зберігання інформації за її змістом чи походженням
person1 = {'name': 'Igor', 'age': 18, 'best_friend': 'Igor'}

person = {
    'name': 'Igor',
    'age': 18,
    'best_friend': 'Igor',
}

empty = None

team = {
    'members_count': 45,
    'sport_types': [
        'chese',
        'soccer',
        'archery',
    ],
    'misty_data': None,
}

set1 = {1, 2, 3, 'hyuf'}

dick_creation_2 = dict()
dick_creation_3 = dict(city='Odesa', village='Myrne')
dick_creation_4 = {}
dick_creation_5 = dict.fromkeys(set1) # другий аргумент буде переданий як значення для всіх
# ключів новоствореного словника, інакше None
print('from keys', dick_creation_5)

