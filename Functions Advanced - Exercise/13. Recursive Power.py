def recursive_power(x, y):
    if y == 0:
        return 1

    if y >= 1:
        return x * recursive_power(x, y - 1)


# print(recursive_power(2, 10))
