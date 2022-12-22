# Write a recursive function which accepts an array of arrays and returns a new array with all values flattened.


def flatten(arr):
    assert type(arr) == list, "This function only accepts list"
    if len(arr) == 0:
        return []
    if type(arr[0]) is list:
        return flatten(arr[0]) + flatten(arr[1:])
    return arr[:1] + flatten(arr[1:])
