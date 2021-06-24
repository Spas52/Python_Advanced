from collections import deque

cups_capacity = deque(list(map(int, input().split())))
filled_bottles = deque(list(map(int, input().split())))
wasted_water = 0

while len(cups_capacity) > 0:
    if len(filled_bottles) <= 0:
        break
    bottle = filled_bottles.pop()
    cup = cups_capacity.popleft()
    filling_cup = cup - bottle
    if filling_cup > 0:
        while filling_cup > 0:
            pick_another_bottle = filled_bottles.pop()
            filling_cup = filling_cup - pick_another_bottle
        if filling_cup < 0:
            wasted_water += abs(filling_cup)
    else:
        wasted_water += abs(filling_cup)

if len(filled_bottles) <= 0:
    result = ""
    while len(cups_capacity) > 0:
        result += str(cups_capacity.popleft()) + ' '
    print(f"Cups: {result}")
else:
    result = ""
    while len(filled_bottles) > 0:
        result += str(filled_bottles.popleft()) + ' '
    print(f"Bottles: {result}")

print(f"Wasted litters of water: {wasted_water}")
