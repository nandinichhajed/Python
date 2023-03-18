lower_range = 400
upper_range = 600

number = int(input("Enter a number: "))

for number in range(lower_range, upper_range + 1):
    if number > 1:
        for i in range(2, number):
            if(number % i == 0):
                break
        else:
            print(number)


