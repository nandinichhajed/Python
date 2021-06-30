picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# # 1
# for row in picture:
#     line = ''
#     for pixel in row:
#         if pixel == 0:
#             line += ' '
#         elif pixel == 1:
#             line += '*'
#     print(line)

# 2
for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end='')
        else:
            # to append any string at the end of the output of the print statement. By default, the print method ends with a newline.
            print('*', end='')
    print(' ')  # to add new line after every row
