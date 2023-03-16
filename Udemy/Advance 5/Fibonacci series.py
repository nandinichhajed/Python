# Here is an example generator which calculates fibonacci numbers:
# generator version

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        a, b = b, b+a


for x in fib(21):
    print(x)

# list method


def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        a, b = b, b+a
    return result


print(fib2(21))
