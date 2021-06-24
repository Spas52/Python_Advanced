def multiply(*args):
    sum = 1
    for el in args:
        sum *= el
    return sum


print(multiply(1, 4, 5))