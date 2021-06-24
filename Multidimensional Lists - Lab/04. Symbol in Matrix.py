n = int(input())
matrix = []

for row in range(n):
    matrix.append(list(input()))

symbol = input()
position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            position = (row, col)
            break
    if position:
        break

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")