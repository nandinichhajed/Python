# squaring
my_list = [5, 4, 3]
print(list(map(lambda item: item**2, my_list)))

# List sorting based on the second element
a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
