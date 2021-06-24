def get_chair_combinations(people, seats, combs=[]):
    if len(combs) == seats:
        print(", ".join(combs))
        return

    for i in range(len(people)):
        name = people[i]
        combs.append(name)
        get_chair_combinations(people[i + 1:], seats, combs)
        combs.pop()


people = [el for el in input().split(', ')]
seats = int(input())
get_chair_combinations(people, seats)