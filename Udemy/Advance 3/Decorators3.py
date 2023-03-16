# decorator pattern :- it gives our decorator flexiblity

def my_decorator(func):  # HOC
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func


@my_decorator
def hello(greeting, emoji='♥'):
    print(greeting, emoji)


hello('hiiii')
