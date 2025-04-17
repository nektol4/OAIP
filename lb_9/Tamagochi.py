class tamagochi:
    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.energy = 100
        self.boring = 30

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            return f'вы покормили {self.name}. уровень голода: {self.hunger}'
        if self.hunger <= 90:
            return f'срочно покормите {self.name}'
        else:
            return f'{self.name} не может переесть'

    def sleep(self):
        if self.enegy < 100:
            self.energy += 40
            return f'{self.name} поспал. уровень энергии: {self.energy}'
        else:
            return f'{self.name} не хочет спать'

    def play(self):
        if self.energy < 100:
            self.energy -= 20
            self.hunger += 20
            self.boring -= 30
            return f'вы поиграли с {self.name}. уровень энерегии {self.energy}. уровень голода {self.hunger}. уровень унылости {self.boring}'
        else:
            return f'{self.name} не хочет играть'

    def status(self):
        if self.hunger and self.boring == 100:
            return f'{self.name} умер.'
        else:
            return f'{self.name} чувствует себя нормально'

a = tamagochi('дфкн')
a.hunger
a.status()