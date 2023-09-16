import functools


@functools.cache
def foo(arg: int):
    print(666)
    return arg * 3


print(foo(10))
