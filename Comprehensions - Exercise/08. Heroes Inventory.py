def get_heroes_items(heroes):
    command = input()
    while command != 'End':
        hero, item, cost = command.split('-')
        cost = int(cost)
        if hero in heroes:
            if item not in heroes[hero]:
                heroes[hero][item] = cost

        else:
            heroes[hero] = {item: cost}
        command = input()
    return heroes


def print_result(heroes):
    for hero, value in heroes.items():
        count_items = 0
        sum_cost = 0
        for item, cost in value.items():
            count_items += 1
            sum_cost += cost
        print(f'{hero} -> Items: {count_items}, Cost: {sum_cost}')


heroes = {s: {} for s in input().split(', ')}
heroes = get_heroes_items(heroes)
print_result(heroes)