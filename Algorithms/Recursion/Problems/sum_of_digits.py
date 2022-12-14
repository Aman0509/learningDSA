# Write a program to find the sum of digits using Recursion


def sum_of_digits(n):
    assert int(n) == n, "Number must be of type int"
    if n == 0:
        return 0
    if n < 0:
        return sum_of_digits(-n)
    return (n % 10) + sum_of_digits(n // 10)
