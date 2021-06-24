n_lines = int(input())
stack = []
maximum = 0
minimum = 0
result = []
for _ in range(n_lines):
    query = input()
    if "1" in query:
        action, number = query.split()
        stack.append(int(number))
    elif "2" in query:
        if len(stack) > 0:
            stack.pop()
    elif "3" in query:
        if len(stack) > 0:
            max_el = max(stack)
            print(max_el)
    elif "4" in query:
        if len(stack) > 0:
            min_el = min(stack)
            print(min_el)

while stack:
    number = stack.pop()
    result.append(str(number))
print(", ".join(result))