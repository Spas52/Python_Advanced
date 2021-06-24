n = int(input())
row = 0
odd_set = set()
even_set = set()
for _ in range(n):
    name = input()
    row += 1
    summary = 0
    for el in name:
        summary += ord(el)
    summary = int(summary / row)
    if summary % 2 == 0:
        even_set.add(summary)
    else:
        odd_set.add(summary)

summary_of_odd = sum(odd_set)
summary_of_even = sum(even_set)

if summary_of_odd == summary_of_even:
    union_values = [str(el) for el in list(odd_set | even_set)]
    print(f"{', '.join(union_values)}")

elif summary_of_odd > summary_of_even:
    different_values = [str(el) for el in list(odd_set - even_set)]
    print(f"{', '.join(different_values)}")

else:
    symmetric_different_values = [str(el) for el in list(odd_set ^ even_set)]
    print(f"{', '.join(symmetric_different_values)}")