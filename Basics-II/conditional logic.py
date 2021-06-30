# condition 1
is_old = True
is_licenced = True
if is_old:
    print('you are old enough to drive')
elif is_licenced:
    print('you can drive now!')
else:
    print('you are not of age!')

print('okok')

# condition 2
is_old = False
is_licenced = True
if is_old:
    print('you are old enough to drive')
elif is_licenced:
    print('you can drive now!')
else:
    print('you are not of age!')

print('okok')

# condition 3
is_old = False
is_licenced = False
if is_old:
    print('you are old enough to drive')
elif is_licenced:
    print('you can drive now!')
else:
    print('you are not of age!')

print('okok')

# condition 4 (and key word)
is_old = True
is_licenced = True
if is_old and is_licenced:
    print('you are old enough to drive, and have a licence ')
else:
    print('you are not of age!')

print('okok')
