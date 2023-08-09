from decimal import Decimal

price = 140.01

price1 = Decimal(str(price)).quantize(Decimal('0.01'))
quantity1 = Decimal(str(1.233)).quantize(Decimal('0.001'))
cost1 = Decimal(quantity1 * price1).quantize(Decimal('0.01'))

price2 = Decimal(str(10.01)).quantize(Decimal('0.01'))
quantity2 = Decimal(str(1.1)).quantize(Decimal('0.001'))
cost2 = Decimal(quantity2 * price2).quantize(Decimal('0.01'))


total_cost = cost1 + cost2

discount = total_cost * Decimal(str(0.05)).quantize(Decimal('0.01'))
final_discount = Decimal(discount).quantize(Decimal('0.01'))

final = total_cost - final_discount

pass
