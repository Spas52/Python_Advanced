def get_combinations(characters, current_index=0):
    if current_index == len(characters):
        print(''.join(characters))
        return

    for i in range(current_index, len(characters)):
        characters[current_index], characters[i] = characters[i], characters[current_index]
        get_combinations(characters, current_index + 1)
        characters[current_index], characters[i] = characters[i], characters[current_index]


characters = list(input())
get_combinations(characters)