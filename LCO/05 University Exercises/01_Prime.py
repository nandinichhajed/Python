number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if(number % i == 0):
            print(number, "is not a prime number")
            print(i, "times", number//i, "is", number)
            break
    else:
        print("%d is prime number" % (number))
