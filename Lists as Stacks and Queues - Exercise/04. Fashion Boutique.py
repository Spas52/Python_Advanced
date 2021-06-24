box = list(map(int, input().split()))  # pravi 2 3 4 5 6 na integers v list
capacity = int(input())

current_capacity = capacity

counter_racks = 1
while len(box) > 0:
    current_v_cloth = box.pop()
    if current_v_cloth <= current_capacity:
        current_capacity -= current_v_cloth
    else:
        counter_racks += 1
        current_capacity = capacity
        current_capacity -= current_v_cloth

print(counter_racks)