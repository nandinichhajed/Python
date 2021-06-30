i = 0
while i < 50:
    print(i)
    i = i+1
    break
else:  # else will be executed if there is no break statement
    print('done with all the work')

# comparing for and while
my_list = [1, 2, 3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1  # or i = i + 1

# most useful ways to use wile loop
while True:
    response = input('say something:')
    if (response == 'bye'):
        break
