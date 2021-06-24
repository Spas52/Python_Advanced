from collections import deque

quantity_of_the_food = int(input())
orders = deque(list(map(int, input().split())))
biggest_order = max(orders)
is_orders_complete = True
print(biggest_order)
while quantity_of_the_food > 0:
    if len(orders) == 0:
        break
    food = orders[0]
    if quantity_of_the_food - food >= 0:
        order = orders.popleft()
        quantity_of_the_food -= order
    else:
        is_orders_complete = False
        break

if is_orders_complete:
    print("Orders complete")
else:
    leftovers = []
    while len(orders) > 0:
        f = str(orders.popleft())
        leftovers.append(f)
    print(f"Orders left: {' '.join(leftovers)}")
