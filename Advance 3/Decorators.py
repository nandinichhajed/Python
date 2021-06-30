# writing our own decorator
# decorator supercharge our function.
# enhance a function or changes it.
# functions are first class citizens.

# basic syntex to create a decorator
#         def my_decorator(func):  #HOC
#             def wrap_func():
#                 func()
#             return wrap_func

def my_decorator(func):  # HOC
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func


@my_decorator
def hello():
    print('hello')


@my_decorator
def bye():
    print('see ya later')


hello()
bye()


# so what we are doing here is:-
# a = hello      and wraping this hello and calling it with my_decorator
# i.e:-    a = my_decorator(hello)
# a()      running a

# wraping my hello function with my_decorator and assigning it to a variable
hello2 = my_decorator(hello)
hello2()

my_decorator(hello)()  # another wa of calling wrap function
# my_decorator recives a function and return the wrap function so now hello2 equals the wrap function
# and then it gets called and print the print statement

# but the best way to do is add my decorator
