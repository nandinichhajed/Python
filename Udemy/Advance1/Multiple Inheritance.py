class user():       # parent class
    def sign_in(self):
        print('logged in')


class wizard(user):  # children classes or derived classes
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attacak(self):
        print(f'attacking with power of {self.power}')


class archer(user):  # children classes or derived classes
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')


class HybridBorg(wizard, archer):
    def __init__(self, name, power, arrows):
        archer.__init__(self, name, arrows)
        wizard.__init__(self, name, power)


hb1 = HybridBorg('nandini', 60, 100)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attacak())
print(hb1.sign_in())
