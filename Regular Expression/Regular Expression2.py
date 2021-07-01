import re
pattern = re.compile('serch this inside of this text please')
string = 'serch this inside of this text please Nandini'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)  # the entire string has to be same to run this
d = pattern.match(string)
e = pattern.split(string)
print(a)
print(b)
print(c)
print(d)
print(e)
