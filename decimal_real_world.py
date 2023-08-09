from decimal import Decimal

strange = 0.2 + 0.1

number = Decimal(strange).quantize(Decimal('0.01'))
print(number)
increase = number + 55
increase2 = number + number
print(increase)
print(increase2)

print('*' * 50)
# unpredictable
number_30_3 = 30.3
num_to_dec = Decimal(str(number_30_3))#.quantize(Decimal('0.01'))
print(num_to_dec)
print(num_to_dec / 3)
print(num_to_dec % 3)
print(num_to_dec // 3)
# print(num_to_dec * 0.6)
print(num_to_dec * 3)


pass
