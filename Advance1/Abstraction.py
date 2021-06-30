class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter('Nandini', 19)

player1.name = '!!!!'
# we have modified speak to a sting value instid of actual function
player1.speak = 'Ahhhh'

print(player1.speak)
