numbers = input().split()
result = []

while numbers:
    result.append(numbers.pop())

print(f"{' '.join(result)}")