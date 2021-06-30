# Error Handling

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(err)


print(sum(1, '2'))


def sum(n1, n2):
    try:
        return n1/n2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum(1, '2'))
