rows, columns = [int(el) for el in input().split()]

matrix = []

# ['A', 'B', 'B', 'D']
# ['E', 'B', 'B', 'B']
# ['I', 'J', 'B', 'B']

for row in range(rows):
    matrix.append(input().split())


found = 0

for row in range(rows-1, 0, -1):
    for col in range(columns-1, 0, -1):
        if matrix[row][col] == matrix[row][col-1] == matrix[row-1][col] == matrix[row-1][col-1]:
            found += 1

print(found)

