def get_int_nums():
    return [int(el) for el in input().split()]


def get_minimum(nums):
    return print(f'The minimum number is {min(nums)}')


def get_maximum(nums):
    return print(f'The maximum number is {max(nums)}')


def get_sum(nums):
    return print(f'The sum number is: {sum(nums)}')


float_nums = get_int_nums()
get_minimum(float_nums)
get_maximum(float_nums)
get_sum(float_nums)