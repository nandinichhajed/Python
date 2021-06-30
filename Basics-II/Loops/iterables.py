# iterable - list, dictonary, tuple, set, string
# iterate -> one by one check each item in the collection.
# int object is not itterable

user = {
    'name': 'Golden',
    'age': 20,
    'can_swin': False
}

for item in user:
    print(item)

# applying methods of dictonary in loops
for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# Tuple unpacking

for keys, values in user.items():
    print(keys, values)
