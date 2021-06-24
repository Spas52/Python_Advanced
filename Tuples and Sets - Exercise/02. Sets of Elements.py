length_of_n, length_of_m = [int(x)for x in input().split()]
n = set()
m = set()
for _ in range(length_of_n):
    number = int(input())
    n.add(number)
for _ in range(length_of_m):
    number = int(input())
    m.add(number)
result = n & m
for num in result:
    print(num)
