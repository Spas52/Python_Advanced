chemical_elements = set()
n = int(input())
for _ in range(n):
    chemical_compounds = input().split()
    for comp in chemical_compounds:
        chemical_elements.add(comp)

for el in chemical_elements:
    print(el)