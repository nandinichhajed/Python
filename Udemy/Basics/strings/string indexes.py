selfish = '01234567'
#  01234567

# [start:stop:stepover]
print(selfish)
print(selfish[7])
print(selfish[0:2])
print(selfish[0:8:1])         # step over by 1
print(selfish[0:8:2])         # step over by 2
print(selfish[1:])            # start at 1 and then go ahead
print(selfish[:5])            # start at 0 and goes to 5
print(selfish[::1])  # start default at 0 end when string end and stepover of 1
print(selfish[-1])   # -ve index means start from backward
# default and stepover of -1 i.e the string willbe printed reversed
print(selfish[::-1])


python = 'I am PYHTON'
print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])
