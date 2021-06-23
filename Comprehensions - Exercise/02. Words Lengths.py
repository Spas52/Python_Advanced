a = [word for word in input().split(', ')]

b = [f'{text} -> {len(text)}' for text in a]
# ['Peter -> 5', 'George -> 6', 'Bill -> 4', 'Lilly -> 5', 'Katy -> 4']

print(", ".join(b))