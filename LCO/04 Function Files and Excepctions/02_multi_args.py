def addme(*num):
    # total = num + num2
    # return total
    total = 0
    for v in num:
        total = total + v
    return total

myVal = addme(3, 5)

print(addme(3, 3, 2, 1, 99, 44, 3))

# task del the values enter by user from MRP (only 2 values allowed)
def my_function(*args):
    if len(args) != 2:
        raise TypeError("my_function() takes 2 arguments")
    arg1, arg2 = args
    total = 100
    total = total - arg1 -arg2
    return total

print(my_function(2, 3, 5))