categories = {cat: [] for cat in input().split(', ')}
# {'food': {}, 'water': {}, 'materials': {}, 'metal': {}}
n = int(input())
count_of_items = 0
quality = 0
for _ in range(n):
    category, item, qq = input().split(' - ')
    # ['food ', ' pizza ', ' quantity:10;quality:5']
    qq = [el.split(':') for el in qq.split(';')]
    # [[' quantity', '10'], ['quality', '5']]
    count_of_items += int(qq[0][1])
    quality += int(qq[1][1])
    for key, value in categories.items():
        if key == category:
            categories[category].append(item)
            break

print(f"Count of items: {count_of_items}")
print(f"Average quality: {(quality/len(categories)):.2f}")
for key, value in categories.items():
    print(f"{key} -> {', '.join(value)}")
