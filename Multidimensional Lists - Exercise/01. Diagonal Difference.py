n = int(input())

matrix = []

# [11, 2,  4]
# [4,  5,   6]
# [10, 8, -12]
primary_diagonal = 0
secondary_diagonal = 0
for row in range(n):
    matrix.append([int(el) for el in input().split()])
    for col in range(n):
        if row == col:
            primary_diagonal += matrix[row][col]
for row in range(n):
    for col in range(n):
        if col == n-1-row:
            secondary_diagonal += matrix[row][col]

diff = abs(primary_diagonal - secondary_diagonal)
print(diff)
