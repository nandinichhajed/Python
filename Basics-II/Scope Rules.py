# prob 1
a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())

# prob 2
a = 1


def confusion():
    a = 5
    return a


print(confusion())
print(a)

# prob 3
a = 1


def confusion():
    return a


print(confusion())
print(a)

# prob 4

a = 1


def parent():
    a = 10

    def confusion():
        return a
    return confusion()


print(parent())
print(a)

# prob 5

a = 1


def parent():
    def confusion():
        return a
    return confusion()


print(parent())
print(a)

# prob 6

a = 1


def parent():
    def confusion():
        return sum
    return confusion()


print(parent())
print(a)

# Rules
# 1. start with local
# 2. Parent local?
# 3. Global
# 4. built in python functions.
