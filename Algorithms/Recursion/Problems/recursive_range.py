# Write a function which accepts a number and adds up all the numbers from 0 to the number passed to the function using recursion


def recursive_range(num):
    assert type(num) == int, "Number must be of type int"
    if num <= 0:
        return 0
    return num + recursive_range(num - 1)
