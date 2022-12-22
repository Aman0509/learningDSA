# Write a function which accepts an array of numbers and return product of them all using recursion


def product_of_array_1(arr):
    assert type(arr) == list, "This function only accepts list"
    if len(arr) == 0:
        return 1
    return arr[0] * product_of_array_1(arr[1:])


def product_of_array_2(arr, i=0):
    assert type(arr) == list, "This function only accepts list"
    try:
        return arr[i] * product_of_array_2(arr, i=i + 1)
    except IndexError:
        return 1
