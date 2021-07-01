# with open('test.txt', 'r') as my_file:
#     print(my_file.readlines())
#     # mode = 'w' -> write
#     # mode = 'r' -> read

# with open('new_text.txt', 'r+') as my_file:
#     # r+ for read & write
#     text = my_file.write('hii people')
#     print(text)


# with open('new_text.txt', 'a') as my_file:
#     # a for append nd this appends to the end of the file
#     text = my_file.write(' cactus here')
#     print(text)


# with open('new_text.txt', 'w') as my_file:
#     # in w oprator it will assume it as a new file and will replace all the content
#     text = my_file.write(' cactus here')
#     print(text)

with open('sad.txt', 'w') as my_file:
    # in w oprator it will assume it as a new file and will replace all the content
    text = my_file.write('oooo')
    print(text)
    # w also creates anew file if it dosent exsists
