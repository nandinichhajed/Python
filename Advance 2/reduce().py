from functools import reduce
my_list = [1, 2, 3]


def accumulatar(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulatar, my_list, 10))
print(my_list)
