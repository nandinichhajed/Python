user_name = input('enter yor user name')
password = input('enter password')
length = len(password)
hidden_password = '*' * length
print(f'{user_name}, your password {hidden_password} is {length} letters long')
