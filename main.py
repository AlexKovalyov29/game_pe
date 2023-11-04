class Enemy:
    health = 0
    attack = 0
    protection = 0

    def __init__(self):
        self.health = self.health
        self.attack = self.attack
        self.protection = self.protection

    def person_speaks_for_himself(self):
        print(f'My class is {self.__class__.__name__},Characteristics: health {self.health},'
              f' damage {self.attack}, protection {self.protection}. And I`m ready to win')



class Orcs(Enemy):
    health = 100
    attack = 20
    protection = 30


class Deathwings(Enemy):
    health = 100
    attack = 35
    protection = 35


class Lichs(Enemy):
    health = 100
    attack = 40
    protection = 35

