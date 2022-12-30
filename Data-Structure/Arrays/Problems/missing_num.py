# How to find the missing number in an integer array of first n natural numbers?


def missing_num(arr, n):
    tot_sum = n * (n + 1) / 2
    arr_sum = sum(arr)
    return tot_sum - arr_sum
