from collections import deque

firework_effects = deque([int(el) for el in input().split(', ')])
# 5, 6, 4, 16, 11, 5, 30, 2, 3, 27
explosive_power = [int(el) for el in input().split(', ')]
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22

firework_dict = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}

is_successfully = True
perfect = 0
while True:
    firework = 0
    if firework_dict['Palm Fireworks'] >= 3:
        if firework_dict['Willow Fireworks'] >= 3:
            if firework_dict['Crossette Fireworks'] >= 3:
                break
    if not firework_effects or not explosive_power:
        is_successfully = False
        break
    if firework_effects[firework] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop(-1)
        continue
    mix_firework = firework_effects[firework] + explosive_power[-1]
    if mix_firework % 3 == 0 and mix_firework % 5 != 0:
        firework_dict['Palm Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop(-1)
    elif mix_firework % 5 == 0 and mix_firework % 3 != 0:
        firework_dict['Willow Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop(-1)
    elif mix_firework % 5 == 0 and mix_firework % 3 == 0:
        firework_dict['Crossette Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop(-1)
    else:
        firework_effects[firework] -= 1
        effect = firework_effects[firework]
        firework_effects.popleft()
        firework_effects.append(effect)

if is_successfully:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
for key, value in firework_dict.items():
    print(f"{key}: {value}")
