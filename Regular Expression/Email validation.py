# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# r is a raw string.
# ^ starting position
# [a-zA-Z0-9_.+-]  start of line it shoud match this
# plus after this is a quantifire so the string can be as long as we want


# @ we must have it
# [a-zA-Z0-9-] after @ it should contain this
# \. it matches the character except line terminator . literally(case sensitive)
# $ end of the line

# import re
# pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# string = 'nandini@gmail.com'
# a = pattern.search(string)
# print(a)

# takin input from user
import re
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
Email = input('Enter your Email:- ')
a = re.search(pattern, Email)
if(a):
    print('valid email')
else:
    print('invalid email')
