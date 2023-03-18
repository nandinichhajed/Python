# m = [[1,2,3], [4,5,6]]
#
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
a = [1, 2, 3]

ROW = int(input("Enter number of Rows: "))
COLUMNS = int(input("Enter number of Columns: "))


matrix = []
print("Enter the values in row: ")

# todo take input in a matrix
for i in range(ROW):
    a = []
    for j in range(COLUMNS):
        a.append(int(input()))
    matrix.append(a)

# TODO print the matrix

for i in range(ROW):
    for j in range(COLUMNS):
        print(matrix[i][j], end=" ")
    print()