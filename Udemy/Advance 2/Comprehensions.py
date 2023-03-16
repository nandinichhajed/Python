# syntex = [param for param in itterable]
# list comprehensions
my_list = [char for char in 'hello']
my_list1 = [num for num in range(0, 100)]
my_list2 = [num**2 for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)

# sets comprehensions
my_list = {char for char in 'hello'}
my_list1 = {num for num in range(0, 100)}
my_list2 = {num**2 for num in range(0, 100)}
my_list3 = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)

# Dictonary comprehensions
simple_dictonary = {
    'a': 1,
    'b': 2
}

my_dict = {k: v**2 for k, v in simple_dictonary.items()}
my_dict1 = {k: v**2 for k, v in simple_dictonary.items() if v % 2 == 0}
my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict)
print(my_dict1)
print(my_dict2)
