import unittest
from Recursion.Problems import (
        sum_of_digits,
        power_of_num,
        gcd
    )

class TestRecursion(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits.sum_of_digits(129), 12)
        self.assertEqual(sum_of_digits.sum_of_digits(-1000), 1)
        self.assertEqual(sum_of_digits.sum_of_digits(5), 5)
        self.assertRaises(AssertionError, sum_of_digits.sum_of_digits, 2.5)

    def test_power_of_num(self):
        self.assertEqual(power_of_num.power_of_num(2,5), 32)
        self.assertEqual(power_of_num.power_of_num(-13,3), -2197)
        self.assertEqual(power_of_num.power_of_num(-7,2), 49)
        self.assertEqual(power_of_num.power_of_num(0.5, 2), 0.25)
        self.assertRaises(AssertionError, power_of_num.power_of_num, 4, 2.1)

    def test_gcd(self):
        self.assertEqual(gcd.gcd(48, 18), 6)
        self.assertEqual(gcd.gcd(36, 60), 12)
        self.assertEqual(gcd.gcd(-10, 5), 5)
        self.assertEqual(gcd.gcd(10, -5), 5)
        self.assertEqual(gcd.gcd(-10, -5), 5)
        self.assertRaises(AssertionError, gcd.gcd, 3.5, 3)
