from pywebio.input import input as pw_input
from pywebio.output import put_success

# user1_favorites = set(str(pw_input('Enter your food', required=True)).lower().split())
# user2_favorite = set(str(pw_input('Enter your food', required=True)).lower().split())
# user3_favorite = set(str(pw_input('Enter your food', required=True)).lower().split())
# user1_favorites = set(input('Enter your food').lower().split())
# user2_favorites = set(input('Enter your food').lower().split())
# user3_favorites = set(input('Enter your food').lower().split())
# common = user1_favorites & user2_favorites & user3_favorites
# put_success(common)
# string_common = ', '.join(common)
string_common = ', '.join(['astr', '67'])
print(f'Your favorite food: {string_common} !!!')

# print(common)
