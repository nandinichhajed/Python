class user(object):       # parent class
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class wizard(user):  # children classes or derived classes
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attacak(self):
        user.attack(self)
        print(f'attacking with power of {self.power}')


class archer(user):  # children classes or derived classes
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attacak(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = wizard('nandini', 60)
archer1 = archer('aastha', 30)

# print(wizard1.attacak())


def player_attack(char):
    char.attack()


# player_attack(wizard1)
# player_attack(archer1)

for char in [wizard1, archer1]:
    char.attacak()
