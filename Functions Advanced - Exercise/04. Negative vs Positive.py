def get_int_nums():
    return [int(el) for el in input().split()]


def get_sum_of_negative(nums):
    negative_nums = list(filter(lambda s: s <= 0, nums))
    return print(sum(negative_nums))


def get_sum_of_positive(nums):
    positive_nums = list(filter(lambda s: s >= 0, nums))
    return print(sum(positive_nums))


def get_stronger(nums):
    negative_nums = abs(sum(list(filter(lambda s: s <= 0, nums))))
    positive_nums = sum(list(filter(lambda s: s >= 0, nums)))
    if negative_nums > positive_nums:
        return print(f'The negatives are stronger than the positives')
    else:
        return print(f'The positives are stronger than the negatives')


float_nums = get_int_nums()
get_sum_of_negative(float_nums)
get_sum_of_positive(float_nums)
get_stronger(float_nums)
