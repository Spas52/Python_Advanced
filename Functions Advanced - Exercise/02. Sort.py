def get_int_nums():
    return [int(el) for el in input().split()]


def sorting(nums):
    nums = sorted(nums)
    return nums


float_nums = get_int_nums()
sorted_numbers = sorting(float_nums)
print(sorted_numbers)