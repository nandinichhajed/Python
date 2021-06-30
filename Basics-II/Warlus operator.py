a = 'helllllooooooo'

if ((n := len(a)) > 10):
    print(f'length of string is too long {n} characters')

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
print(a)
