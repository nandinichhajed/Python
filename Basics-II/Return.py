def sum(num1, num2):
    return num1 + num2


# a function should do one thing really well
# should return something
total = sum(4, 5)
print(sum(4, total))  # print(sum(4, sum(4, 5)))


def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)


# a return keyword automatecally exit the function
print('hellooo')  # function has already exit
total = sum(4, 5)
print(total)
