
class GoodPerson:
    name = ''
    health = 0
    attack = 0
    protection = 0

    def __init__(self):
        self.name = self.name
        self.health = self.health
        self.attack = self.attack
        self.protection = self.protection

    def person_speaks_for_himself(self):
        print(f'My name is {self.name},my class is {self.__class__.__name__},Characteristics: health {self.health},'
              f' damage {self.attack}, protection {self.protection}. And I`m ready to win')


class Archers(GoodPerson):
    name = 'Luke'
    health = 100
    attack = 30
    protection = 70


class Knights(GoodPerson):
    name = 'Eric'
    health = 100
    attack = 50
    protection = 50


class Wizards(GoodPerson):
    health = 100
    attack = 70
    protection = 30

if __name__ == "__main__":
    test_wizards = Wizards()
    test_wizards.person_speaks_for_himself()




