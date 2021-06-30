# OOP
class PlayerCharacter:
    membership = True  # class object atribute

    def __init__(self, name, age):
        if (self.membership):  # self refers to PlayerCharacter
            self.name = name  # attribute
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        return 'done'

    def run(self, hello):
        print('run')
        return 'done'


player1 = PlayerCharacter('Nandini', 19)  # instances
player2 = PlayerCharacter('Aastha', 20)
player2.attack = 50

print(player1.membership)
print(player2.membership)

print(player1.name)
print(player2.name)

print(player1.shout())
print(player2.shout())

print(player1.age)
print(player2.age)

print(player1.run('hello'))

print(player2.attack)
