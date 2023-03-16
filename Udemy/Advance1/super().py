class user(object):       # parent class
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class wizard(user):  # children classes or derived classes
    def __init__(self, name, power, email):
        super().__init__(email)
        # user.__init__(self, email)   either super keyword ot this user method
        self.name = name
        self.power = power

    def attacak(self):
        print(f'attacking with power of {self.power}')


wizard1 = wizard('nandini', 60, 'chhajed@gmail.com')

print(wizard1.email)
