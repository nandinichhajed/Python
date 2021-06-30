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
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attacak(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = wizard('nandini', 50)
archer1 = archer('aastha', 100)

print(wizard1.sign_in())

wizard1.attacak()
archer1.attacak()


# isinstance(isinstance, class) isinstance is a buildin function
wizard1 = wizard('archit', 60)

print(isinstance(wizard1, wizard))  # wizard1 ia an instance of wizard
print(isinstance(wizard1, user))   # wizard1 ia an instance of user
print(isinstance(wizard1, object))
