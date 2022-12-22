# Write a function to identify if the passed string in it is a palindrome or not using recursion


def is_palindrome(st):
    assert str(st) == st, "This function only accepts strings"
    if len(st) <= 1:
        return True
    return st[0] == st[-1] and is_palindrome(st[1:-1])
