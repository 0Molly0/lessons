# file = open('my.txt', mode='r')
# file.write('pon\n')
# file.close()
import datetime
import functools


# with open('my.txt', mode='a', encoding='utf-8') as file:
#     file.write('duyktdeyhmtde')
#     print(file)


def logger(file_name='log_data.csv'):
    def wrapper1(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            with open(file_name, mode='a', encoding='utf-8') as file:
                file.write(f'{datetime.datetime.now()};{func.__name__};{result}\n')

            return result
        return wrapper
    return wrapper1


@logger()
def foo(arg):
    return arg * 2


@logger()
def foo2(arg):
    return arg * 2


foo(7)


with open('log_data.csv', mode='r', encoding='utf-8') as file:
    # print(file.read())
    # print(file.readline())
    # print(file.readline())
    for line in file.readlines():
        print(line)
        data = line.split(';')
        print(data)
        if data[1] == 'foo2':
            print(data[0])
