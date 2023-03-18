class Samsung:
    def __init__(self):
        print("I am Samsung")

    def makeScreen(self):
        print("I make screens : Samsung")

    def test(self):
        print("Screen test 1: OK")
        print("Screen test 2: OK")
        print("Screen test 3: OK")


class Iphone(Samsung):
    def __init__(self):
        print("I am Iphone")
        # super().__init__()

    def a3chips(self):
        print("I make A3 bionic chips")

    def itest(self):
        print("A3 test: OK")
        super().test()

    def makeScreen(self):
        print("I make screens: Apple")



user = Iphone()

user.a3chips()
user.makeScreen()
user.itest()
user.makeScreen()