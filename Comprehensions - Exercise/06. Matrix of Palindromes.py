rows, columns = [int(el) for el in input().split()]

# matrix = [[chr(column+97) for column in range(columns)] for row in range(rows)]
matrix = []
for row in range(rows):
    matrix.append([])
    for col in range(columns):
        matrix[row].append(chr(97+row) + chr(97+row+col) + chr(97+row))

for row in range(rows):
    print(" ".join(matrix[row]))