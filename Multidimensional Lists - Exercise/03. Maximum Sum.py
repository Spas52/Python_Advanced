import sys

rows, columns = [int(el) for el in input().split()]

matrix = []

# ['1', '5', '5', '2', '4']
# ['2', '1', '4', '14', '3']
# ['3', '7', '11', '2', '8']
# ['4', '8', '12', '16', '4']

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

max_sum = - sys.maxsize
position = None

for row in range(rows-1, 1, -1):
    for col in range(columns-1, 1, -1):
        current_sum = matrix[row][col] + matrix[row][col-1] + matrix[row][col-2] + matrix[row-1][col] + matrix[row-1][col-1] + matrix[row-1][col-2] + matrix[row-2][col] + matrix[row-2][col-1] + matrix[row-2][col-2]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)

row, col = position
print(f"Sum = {max_sum}")
print(matrix[row-2][col-2], matrix[row-2][col-1], matrix[row-2][col])
print(matrix[row-1][col-2], matrix[row-1][col-1], matrix[row-1][col])
print(matrix[row][col-2], matrix[row][col-1], matrix[row][col])