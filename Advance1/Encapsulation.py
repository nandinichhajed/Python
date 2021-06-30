class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'My name is {self.name} and I am {self.age} years old')
        return 'done'


player1 = PlayerCharacter('Nandini', 19)
player1.shout()
