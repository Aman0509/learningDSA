# Write a function which accepts an integer and returns it's corresponding to binary using recursion


def dec_to_bin(n):
    assert int(n) == n, "Number must be of type int"
    if n == 0:
        return 0
    return n % 2 + 10 * dec_to_bin(int(n / 2))
