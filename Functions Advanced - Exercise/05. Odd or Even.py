def get_int_nums():
    return [int(el) for el in input().split()]


def get_sum(action, nums):
    if action == "Odd":
        odd_nums = sum(list(filter(lambda s: s % 2 != 0, nums)))
        return print(f'{odd_nums * len(nums)}')
    elif action == "Even":
        even_nums = sum(list(filter(lambda s: s % 2 == 0, nums)))
        return print(f'{even_nums * len(nums)}')


command = input()
float_nums = get_int_nums()
get_sum(command, float_nums)
