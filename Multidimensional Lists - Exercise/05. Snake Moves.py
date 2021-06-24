from collections import deque

(rows_count, columns_count) = map(int, input().split())
matrix = []
for row_index in range(rows_count):
    row = []
    for c in range(columns_count):
        row.append('a')
    matrix.append(row)
data = input()
snake = deque([])
for ch in data:
    snake.append(ch)
for r in range(rows_count):
    row = deque([])
    for c in range(columns_count):
        current_move = snake.popleft()
        snake.append(current_move)
        if r % 2 == 0:
            row.append(current_move)
        else:
            row.appendleft(current_move)
    print(''.join(str(s) for s in row))
