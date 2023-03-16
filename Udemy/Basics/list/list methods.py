basket = [1, 2, 3, 4, 5]

# adding
basket.append(100)
new_list = basket
print(basket)
print(new_list)

# insert
basket.insert(4, 100)
new_list = basket
print(basket)
print(new_list)

# extend
new_list = basket.extend([100, 101])
print(basket)

# removing
new_list = basket.extend([100, 101])
basket.pop()  # remove the last item
basket.pop(0)  # we give the index we waana remove
print(basket)
basket.remove(4)  # we give the value we waana remove
print(basket)
basket.clear()
print(basket)

# index
basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d'))
print(basket.index('d', 0, 4))
print('d' in basket)
print('x' in basket)
print('i' in 'Hii')

# count
print(basket.count('d'))

# sort
basket = ['a', 'b', 'x', 'e', 'd', 'c']
basket.sort()
print(basket)
new_basket = basket[:]   # new_basket = basket.copy()
new_basket.sort()
print(new_basket)
print(basket)

# reverse
basket.sort()
basket.reverse()
print(basket)
print(basket[::-1])  # slicing create the copy of list
print(basket)

# range
print(range(1, 100))
print(list(range(1, 100)))
print(list(range(100)))

# join
new_sentence = ' '.join(['Hi', 'my', 'name', 'is', 'Nandini'])
print(new_sentence)

# list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
