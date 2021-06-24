rows, columns = [int(el) for el in input().split()]

matrix = []

# [1, 2, 3]
# [4, 5, 6]

for row in range(rows):
    matrix.append(input().split())
command = input()
while command != "END":
    data = command.split()
    if data[0] != "swap":
        print("Invalid input!")
        command = input()
        continue
    elif len(data) != 5:
        print("Invalid input!")
        command = input()
        continue
    elif len(data) == 5:
        row1 = int(data[1])
        col1 = int(data[2])
        row2 = int(data[3])
        col2 = int(data[4])
        if row1 not in range(len(matrix)) or row2 not in range(len(matrix)):
            print("Invalid input!")
            command = input()
            continue
        elif col1 not in range(len(matrix[0])) or col2 not in range(len(matrix[0])):
            print("Invalid input!")
            command = input()
            continue
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in range(rows):
                result = [str(el) for el in matrix[row]]
                print(" ".join(result))
    command = input()



