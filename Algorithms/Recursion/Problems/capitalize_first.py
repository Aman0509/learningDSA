# Write a recursive function which capitalize the first letter of each string in the array.


def capitalize_first(arr):
    assert type(arr) == list, "This function only accepts list"
    if len(arr) == 0:
        return []
    return [arr[0][0].upper() + arr[0][1:]] + capitalize_first(arr[1:])
