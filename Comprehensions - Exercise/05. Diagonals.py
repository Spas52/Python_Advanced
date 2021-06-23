n = int(input())

matrix = [[int(s) for s in (input().split(', '))]for i in range(n)]

primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    for col in range(n):
        if row == col:
            primary_diagonal.append(matrix[row][col])

for row in range(n):
    for col in range(n):
        if col == n-1-row:
            secondary_diagonal.append(matrix[row][col])

print(f"First diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Second diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
