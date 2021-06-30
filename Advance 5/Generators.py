# Generators are subset of iterables
# everything that is generator is iterable but viceversa is not true


def generator_function(num):
    for i in range(num):
        yield i*2     # yeild pause the function


g = generator_function(100)
next(g)
next(g)
print(next(g))


# for item in generator_function(1000):
#     print(item)
