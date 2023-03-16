# ==
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# is (checks for equaliuty and value)
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])

#  corrected is
print(True is True)
print('1' is '1')
# both list are at different location so have different memory.
print([] is [])
print(10 is 10)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
