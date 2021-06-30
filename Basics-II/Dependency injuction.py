# Depencency injection
total = 0


def count(total):
    total += 1
    return total


print(count(count(count(total))))
