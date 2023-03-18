# only available to positive

# for negative =  NO
# for 0 : 1
# for example: 5
#
# 1*2*3*4*5
#
# 5*4*3*2*1
#
# 3*2
# 2*3


number = 5

factorial = 1

if number < 0:
    print("We don't calculate negative factorials")
elif number == 0:
    print("The result is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The result is", factorial)