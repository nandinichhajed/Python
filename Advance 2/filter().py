my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(filter(multiply_by2, my_list)))
print(my_list)
