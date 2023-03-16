my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# difference
print(my_set.difference(your_set))

# discard - it modifies our set
print(my_set.discard(5))
print(my_set)

# difference_update
print(my_set.difference_update(your_set))
print(my_set)

# intersection
print(my_set.intersection(your_set))

# isjoint
print(my_set.isdisjoint(your_set))

# union
print(my_set.union(your_set))
print(my_set | (your_set))  # another symbol  for union


my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# issubset
print(my_set.issubset(your_set))

# issuperset
print(your_set.issuperset(my_set))
