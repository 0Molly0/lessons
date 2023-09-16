def multiply_classic(number):
    return number * 2


functions = {
    'multiply_classic': multiply_classic,
    'multiply_lambda': lambda number: number * 2,
    'multiply_lambda2': lambda number: number * 2,
}

print(functions['multiply_classic'](5))
print(functions['multiply_lambda'])
print(functions['multiply_lambda2'])

universal = lambda number: print(
    number,
    lambda x: x,
)

print(universal(555))
print(universal(10))
