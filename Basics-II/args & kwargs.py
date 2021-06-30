# *args
def super_func(*args):
    print(*args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5))


# **kwargs
def super_func(name, *args, i='hii', **kwargs):
    total = 0
    for iteams in kwargs.values():
        total += iteams
    return sum(args) + total

    #             rule: Prams, *args, i='hii, **kwargs
print(super_func('Nanni', 1, 2, 3, 4, 5, num1=5, num=10))
