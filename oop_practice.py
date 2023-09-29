from abc import ABC, abstractmethod

import config


class Character(ABC):
    @abstractmethod
    def attack(self, other):
        pass

    def __init__(self, *, name: str, surname=None):
        self.name = name
        self.surname = surname or ''
        self.health_points = 100

    @property
    def is_alive(self):
        return self.health_points > 0

    def __str__(self):
        return f'{self.name}'


class Beast(Character):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.power = config.BeastParameters.POWER
        self.accuracy = config.BeastParameters.ACCURACY
        self.health_points = config.BeastParameters.HEALTH_POINTS

    def attack(self, other):
        raise NotImplemented


class Troll(Character):
    def __init__(self, name):
        super().__init__(name=name)
        self.power = config.TrollParameters.POWER
        self.accuracy = config.BeastParameters.ACCURACY

    def attack(self, other: Character):
        print(f'{self.name.title()} is attacking {other.name.title()}')
        if self == other:
            return
        other.health_points -= self.power
        if not other.is_alive:
            print(f'{self} won')


class SuperTroll(Troll):
    pass


troll = Troll('Sans')
troll2 = Troll('You')
troll.attack(troll2)

print(troll2.name, troll2.health_points, troll2.is_alive)
