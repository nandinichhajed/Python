# methods

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'x': 3
}
user2 = dict(name='Nandini')
print(user['basket'])

# get
print(user.get('age'))
print(user.get('age', 55))
print(user2)

print('basket' in user)
print('size' in user)

# keys
print('x' in user.keys())

# values
print('hello' in user.values())

# items
print(user.items())

# clear
user.clear()  # print(user.clear())
print(user)

# copy
user2 = user.copy()
print(user)
print(user2)

# pop
print(user.pop('x'))
print(user.popitem())
print(user)

# update
print(user.update({'x': 55}))
print(user)
