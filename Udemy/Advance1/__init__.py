class PlayerCharacter:
    membership = True  # class object atribute

    def __init__(self, name='anonymous', age=0):
        if (age > 18):  # self refers to PlayerCharacter
            self.name = name  # attribute
            self.age = age
        else:
            print('player is not old enough')

    def shout(self):
        print(f'my name is {self.name}')
        return 'done'


player1 = PlayerCharacter('Nandini', 19)  # instances

print(player1.shout())
