my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)  # returns only unique vqlues
print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))
print(1 in my_set)
print(len(my_set))
print(list(my_set))
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)  # empty set
