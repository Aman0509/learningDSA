# Write a program to calculate power of given number using recursion


def power_of_num(n, p):
    assert int(p) == p, "Power must be of type int"
    if p == 0:
        return 1
    elif p < 0:
        return 1 / (n * power_of_num(n, p + 1))
    return n * power_of_num(n, p - 1)
