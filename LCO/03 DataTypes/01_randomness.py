import random
print(random.choice(range(100)))
print(random.choice([1, 2, 3, 4, 5, 6]))
print(random.choice("NandiniChhajed"))

print(random.randrange(1, 100, 2))
# prints a random no between 0 to 1
print(random.random())

# gives the same value
random.seed(10)
print(random.random())

list_numbers = [22, 333, 66, 33, 22, 4]
random.shuffle(list_numbers)
print(list_numbers)
