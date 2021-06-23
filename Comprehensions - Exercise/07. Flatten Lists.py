numbers = [el.split() for el in input().split('|')[::-1]]
result = []
for num in numbers:
    for n in num:
        result.append(n)
print(" ".join(result))