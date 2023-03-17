# import nandini

from nandini import *

# val = nandini.addme(3, 3)
print('''Choose a number to perform operations
        1 = addition
        2 = substraction''')

a = int(input("Enter a no: "))

x = int(input("Enter a no x to perform operation: "))
y = int(input("Enter a no y to perform operation: "))


if a == 1:
    print(addme(x, y))
elif a == 2:
    print(subme(x, y))
else:
    print("Enter either 1 or 2")