# Write a function which accepts 2 integers and return their GCD using recursion
# Info: GCD is the largest positive integer that divides the numbers without a remainder


def gcd_decorator(func):
    def inner(n1, n2):
        n1, n2 = abs(n1), abs(n2)
        return func(n1, n2)

    return inner


@gcd_decorator
def gcd(n1, n2):
    """
    Euclidean Algorithm
    """
    assert int(n1) == n1 and int(n2) == n2, "Numbers must be of type int"
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)
