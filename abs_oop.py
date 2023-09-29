from abc import ABC, abstractmethod

import datetime
import time


class Mammal(ABC):
    def drink(self):
        print('I am drinking')

    @abstractmethod
    def run(self, name):
        pass


class Cow(Mammal):
    def run(self, name):
        print(f'{name} is running')


class Human(Mammal):
    def __init__(self):
        self.birth = datetime.datetime.now()
        print(self.birth)
        self.money = 0

    @property
    def age(self):
        return datetime.datetime.now() - self.birth

    def run(self, name):
        print(f'Human {name} is running very slow')


# mammal = Mammal()
# mammal.drink()
cow = Cow()
human = Human()
human.money += 500

cow.drink()
human.drink()
time.sleep(2)
print(human.age)

cow.run('Tommy')
cow.run('Milly')
print(human.__dict__)
