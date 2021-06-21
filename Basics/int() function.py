# case 1
# example 1
num = 13
string = 187
result_1 = int(string) + num
print("int('187') + 13 = ", result_1, "\n")

# example 2
str = '100'
print("int ('100') with base 2 = ", int(str, 2))
print("int ('100') with base 4 = ", int(str, 4))
print("int ('100') with base 8 = ", int(str, 8))
print("int ('100') with base 16 = ", int(str, 16))
print("int ('100') with base 32 = ", int(str, 32))

# case 2
binarystring = "111"
decimal = int(binarystring, 2)
print("decimal equivelent of binary 111 is", decimal)

octalString = "101"
Octal = int(octalString, 8)
print("Decimal equivalent of octal 101 is", Octal)
