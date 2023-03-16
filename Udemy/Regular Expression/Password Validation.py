# atlist 8 char long
# contain any sort of letters, numbers and $%#@
# has to end with a no


# import re
# pattern = re.compile(r"([A-Za-z0-9$%#@]{8,}[0-9])")

# string = 'nngtja5251jkx85'
# a = pattern.fullmatch(string)
# print(a)


# takin input from user
import re
pattern = re.compile(r"([A-Za-z0-9$%#@]{8,}[0-9])")
password = input('Enter your password:- ')
a = re.fullmatch(pattern, password)
if (a):
    print('valid password')
else:
    print('invalid password')
