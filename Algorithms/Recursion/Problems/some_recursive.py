# Write a recursive function which accepts an array and a callback. The function returns true if a single value in
# the array returns true when passed to the callback. Otherwise it returns false.


def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def some_recursive(arr, cb):
    assert type(arr) == list, "This function only accepts list"
    if len(arr) == 0:
        return False
    return cb(arr[0]) or some_recursive(arr[1:], cb)
