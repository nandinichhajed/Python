picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_tree():
    for row in picture:
        for pixel in row:
            if pixel == 0:
                print(' ', end='')
            else:
                print('*', end='')
        print(' ')


show_tree()
show_tree()
show_tree()
