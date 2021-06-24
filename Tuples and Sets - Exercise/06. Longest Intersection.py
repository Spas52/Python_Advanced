n = int(input())
the_longest_intersection = 0
the_longest_numbers = []
for _ in range(n):
    first_range, second_range = input().split('-')
    first_range = [int(el) for el in first_range.split(',')]
    second_range = [int(el) for el in second_range.split(',')]
    first = set()
    second = set()
    for num in range(first_range[0], first_range[1] + 1):
        first.add(num)
    for num in range(second_range[0], second_range[1] + 1):
        second.add(num)
    length = len(first & second)
    if the_longest_intersection < length:
        the_longest_intersection = length
        the_longest_numbers = []
        for num in (first & second):
            the_longest_numbers.append(num)

print(f'Longest intersection is {the_longest_numbers} with length {the_longest_intersection}')