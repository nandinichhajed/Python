# Truthy

is_old = bool('hello')
is_licenced = bool(5)

print(bool('hello'))
print(bool(5))
if is_old:
    print('you are old enough to drive')
elif is_licenced:
    print('you can drive now!')
else:
    print('you are not of age!')

print('okok')

# Falsy

is_old = bool('hello')
is_licenced = bool(5)

print(bool(''))
print(bool())

if is_old:
    print('you are old enough to drive')
elif is_licenced:
    print('you can drive now!')
else:
    print('you are not of age!')

print('okok')
