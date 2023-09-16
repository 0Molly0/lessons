import copy

number = [6, 5]


def foo(arg: int = number):
    return arg * 3


# print(foo)
# print(foo(6))


def bad(arg: list = None):
    arg = copy.copy(arg)
    if not arg:
        arg = []
    arg.append(3)
    print(id(arg))

    return arg


a = [6]
print(id(a))
print(bad())
print(bad())
print(bad(a))
print(bad(a))
print(bad(a))
print(a)
