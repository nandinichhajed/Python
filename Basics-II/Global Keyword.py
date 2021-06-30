# local variable
a = 10


def confusion(b):  # b is a local variable
    print(b)
    a = 90


confusion(300)

# Global variable

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())
