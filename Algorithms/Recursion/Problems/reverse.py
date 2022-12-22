# Write a function which accepts a string and returns a new string in reverse.


def reverse(st):
    assert str(st) == st, "This function only accepts strings"
    if len(st) == 0:
        return ""
    return st[-1] + reverse(st[:-1])
