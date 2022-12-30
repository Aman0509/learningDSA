# Write a function to find if a passed array has all unique elements


def is_unique(arr):
    d = {}
    if len(arr) == 0:
        raise Exception("Length of list cannot be zero")
    for i in arr:
        ele = d.get(i)
        if ele:
            return False
        d[i] = 1
    return True
