n = int(input())

matrix = [[int(s) for s in (input().split(' '))]for i in range(n)]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
command = input()
while command != "END":
    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    is_valid = True
    if action == "Add":
        if 0 <= row <= len(matrix)-1:
            if 0 <= col <= len(matrix)-1:
                matrix[row][col] += value
            else:
                is_valid = False
        else:
            is_valid = False
    elif action == "Subtract":
        if 0 <= row <= len(matrix)-1:
            if 0 <= col <= len(matrix)-1:
                matrix[row][col] -= value
            else:
                is_valid = False
        else:
            is_valid = False
    if not is_valid:
        print("Invalid coordinates")

    command = input()

for row in range(len(matrix)):
    print(" ".join([str(s) for s in matrix[row]]))


