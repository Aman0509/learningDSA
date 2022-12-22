# Write a recursive function to calculate total diagonals possible for a given polynomial.

"""
Formula for calculating number of diagonals for a given polynomial
n = (n*(n-3))/2
Also,
Check out this video - https://www.brightstorm.com/math/geometry/reasoning-diagonals-angles-and-parallel-lines/number-of-diagonals-in-a-polygon/
"""


def total_diagonals(no_of_sides):
    if no_of_sides < 4:
        return 0
    return (no_of_sides - 2) + total_diagonals(no_of_sides - 1)
