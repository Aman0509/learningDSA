# Write a recursive function to find out the number of total handshakes between 'n' number of individuals.


"""
Formula for calculating number of handshakes
n = (n*(n-1))/2
Also,
Check out this article - http://mason.gmu.edu/~jsuh4/impact/Handshake_Problem%20teaching.pdf
"""


def total_handshakes(total_people):
    assert type(total_people) is int, "This function accepts argument of type int"
    if total_people < 2:
        return 0
    return total_people - 1 + total_handshakes(total_people - 1)
