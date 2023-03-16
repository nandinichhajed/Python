# Type conversion (converting type of datatype)

print(str(100))
print(type(str(100)))
print(type(int(str(100))))

# alternative
a = str(100)
b = int(a)
c = type(b)
print(c)
