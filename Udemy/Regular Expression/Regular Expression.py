import re
string = 'serch inside of this text please'
print('serch' in string)
print(re.search('this', string))
#        serch(pattern, string, flags)
a = re.search('this', string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())
