some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)
print('')
