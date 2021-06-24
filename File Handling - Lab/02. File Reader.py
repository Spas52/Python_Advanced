with open('numbers.txt', 'r') as file:
    numbers = [int(num) for num in file.readlines()]
    print(sum(numbers))