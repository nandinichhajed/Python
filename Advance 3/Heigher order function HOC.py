# a heigher order function is a function that accepts a function as aparameter or returns a function

def greet(func):
    func()


def greet2(func):
    def func():
        return 5
    return func
