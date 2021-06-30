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

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('lilo', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Nandini', 19)  # instances
player2 = PlayerCharacter('Aastha', 20)
player3 = player1.adding_things(2, 3)
print(player3.age)
