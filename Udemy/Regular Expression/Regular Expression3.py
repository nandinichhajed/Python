import re
pattern = re.compile(r"([a-zA-z]).([a])")
string = 'serch this inside of this text please Nandini'
# . matches any character except line terminator
# r is a rew string.
a = pattern.search(string)
print(a.group())
print(a.group(1))
print(a.group(2))
