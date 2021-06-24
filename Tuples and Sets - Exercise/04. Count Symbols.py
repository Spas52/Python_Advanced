occurrences = {}
text = input()
for el in text:
    if el not in occurrences:
        occurrences[el] = 0
    occurrences[el] += 1

sorted_result = sorted(occurrences.items(), key=lambda x: x[0])

for key, value in sorted_result:
    print(f'{key}: {value} time/s')