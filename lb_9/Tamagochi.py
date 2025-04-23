class tamagochi:
    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.energy = 70
        self.boring = 30
        self.life = True

    def feed(self):
        if not self.life:
            print(f'{self.name} мертв')
            return

        if self.hunger > 0:
            self.hunger -= 10
        else:
            print(f'{self.name} не хочет есть')
            self.status()

    def sleep(self):
        if not self.life:
            print(f'{self.name} мертв.')
            return

        if self.energy < 100:
            self.energy += 20
        else:
            print(f'{self.name} не хочет спать')
        self.status()

    def play(self):
        if not self.life:
            print(f'{self.name} мертв')
            return

        if self.energy > 20 and self.boring > 0:
            self.energy -= 20
            self.hunger += 20
            self.boring -= 10
        else:
            print(f'{self.name} не хочет играть')
        self.status()

    def status(self):
        if not self.life:
            print(f'{self.name} мертв.')
            return

        if self.hunger >= 100 or self.boring <= 0 or self.energy <= 0:
            print(f'{self.name} в плохом состоянии.')
            if self.hunger >= 100:
                print(f'{self.name} голоден')
                self.life = False
            if self.boring <= 0:
                print(f'{self.name} скучает')
                self.life = False
            if self.energy <= 0:
                print(f'{self.name} устал')
                self.life = False
        else:
            print(f'Энергия: {self.energy}, Голод: {self.hunger}, Скука: {self.boring}')


