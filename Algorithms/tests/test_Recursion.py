import unittest
from Recursion.Problems import (
    sum_of_digits,
    power_of_num,
    gcd,
    dec_to_bin,
    product_of_array,
    recursive_range,
    reverse,
    is_palindrome,
    some_recursive,
    flatten,
    capitalize_first,
    nested_even_sum,
    capitalize_words,
    stringify_numbers,
    collect_strings,
    total_handshakes,
    total_diagonals,
)


class TestRecursion(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits.sum_of_digits(129), 12)
        self.assertEqual(sum_of_digits.sum_of_digits(-1000), 1)
        self.assertEqual(sum_of_digits.sum_of_digits(5), 5)
        self.assertRaises(AssertionError, sum_of_digits.sum_of_digits, 2.5)

    def test_power_of_num(self):
        self.assertEqual(power_of_num.power_of_num(2, 5), 32)
        self.assertEqual(power_of_num.power_of_num(-13, 3), -2197)
        self.assertEqual(power_of_num.power_of_num(-7, 2), 49)
        self.assertEqual(power_of_num.power_of_num(0.5, 2), 0.25)
        self.assertRaises(AssertionError, power_of_num.power_of_num, 4, 2.1)

    def test_gcd(self):
        self.assertEqual(gcd.gcd(48, 18), 6)
        self.assertEqual(gcd.gcd(36, 60), 12)
        self.assertEqual(gcd.gcd(-10, 5), 5)
        self.assertEqual(gcd.gcd(10, -5), 5)
        self.assertEqual(gcd.gcd(-10, -5), 5)
        self.assertRaises(AssertionError, gcd.gcd, 3.5, 3)

    def test_dec_to_bin(self):
        self.assertEqual(dec_to_bin.dec_to_bin(10), 1010)
        self.assertEqual(dec_to_bin.dec_to_bin(-10), 1010)
        self.assertRaises(AssertionError, dec_to_bin.dec_to_bin, 10.10)

    def test_product_of_array(self):
        self.assertEqual(product_of_array.product_of_array_1([1, 3, 1, 5]), 15)
        self.assertEqual(product_of_array.product_of_array_1([0]), 0)
        self.assertEqual(product_of_array.product_of_array_1([]), 1)
        self.assertRaises(AssertionError, product_of_array.product_of_array_1, "1234")
        self.assertRaises(AssertionError, product_of_array.product_of_array_1, 1234)
        self.assertEqual(product_of_array.product_of_array_2([1, 3, 1, 5]), 15)
        self.assertEqual(product_of_array.product_of_array_2([0]), 0)
        self.assertEqual(product_of_array.product_of_array_2([]), 1)
        self.assertRaises(AssertionError, product_of_array.product_of_array_2, "1234")
        self.assertRaises(AssertionError, product_of_array.product_of_array_2, 1234)

    def test_recursive_range(self):
        self.assertEqual(recursive_range.recursive_range(10), 55)
        self.assertEqual(recursive_range.recursive_range(0), 0)
        self.assertEqual(recursive_range.recursive_range(800), 320400)
        self.assertEqual(recursive_range.recursive_range(-10), 0)
        self.assertRaises(AssertionError, recursive_range.recursive_range, "12345")

    def test_reverse(self):
        self.assertEqual(reverse.reverse("Hello World!"), "!dlroW olleH")
        self.assertEqual(reverse.reverse("HHH"), "HHH")
        self.assertRaises(AssertionError, reverse.reverse, [1, 2, 3, 4])
        self.assertRaises(AssertionError, reverse.reverse, 1234)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome.is_palindrome("tacocat"))
        self.assertFalse(is_palindrome.is_palindrome("banana"))
        self.assertFalse(is_palindrome.is_palindrome("am"))
        self.assertTrue(is_palindrome.is_palindrome("b"))
        self.assertTrue(is_palindrome.is_palindrome(""))
        self.assertRaises(AssertionError, is_palindrome.is_palindrome, [1, 2, 3, 4])
        self.assertRaises(AssertionError, is_palindrome.is_palindrome, 1234)

    def test_some_recursive(self):
        self.assertFalse(
            some_recursive.some_recursive([2, 4, 8, 10], some_recursive.is_odd)
        )
        self.assertTrue(
            some_recursive.some_recursive([6, 9, 10], some_recursive.is_odd)
        )
        self.assertFalse(some_recursive.some_recursive([], some_recursive.is_odd))
        self.assertRaises(
            AssertionError, some_recursive.some_recursive, "1234", some_recursive.is_odd
        )
        self.assertRaises(
            AssertionError, some_recursive.some_recursive, 1234, some_recursive.is_odd
        )

    def test_flatten(self):
        self.assertEqual(
            flatten.flatten([[1, 2, 3], [4], 5, 6, [7], []]), [1, 2, 3, 4, 5, 6, 7]
        )
        self.assertEqual(flatten.flatten([1, [2, [3, 4], [[5]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten.flatten([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(
            flatten.flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]), [1, 2, 3]
        )
        self.assertEqual(flatten.flatten([[], [], []]), [])
        self.assertRaises(AssertionError, flatten.flatten, "1234")

    def test_capitalize_first(self):
        self.assertEqual(
            capitalize_first.capitalize_first(["car", "taco", "banana"]),
            ["Car", "Taco", "Banana"],
        )
        self.assertEqual(
            capitalize_first.capitalize_first(["caR", "tAco", "banAna"]),
            ["CaR", "TAco", "BanAna"],
        )
        self.assertEqual(capitalize_first.capitalize_first(["1Adsa"]), ["1Adsa"])
        self.assertEqual(capitalize_first.capitalize_first([]), [])
        self.assertRaises(AssertionError, capitalize_first.capitalize_first, "1234")

    def test_nested_even_sum(self):
        obj1 = {
            "outer": 2,
            "obj": {
                "inner": 2,
                "otherObj": {
                    "superInner": 2,
                    "notANumber": True,
                    "alsoNotANumber": "yup",
                },
            },
        }
        obj2 = {
            "a": 2,
            "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
            "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
            "d": 1,
            "e": {"e": {"e": 2}, "ee": "car"},
        }
        obj3 = {"a": {"b": {}}, "c": 1}
        obj4 = {"a": 1, "b": 4, "c": {"d": 9}}
        self.assertEqual(nested_even_sum.nested_even_sum(obj1), 6)
        self.assertEqual(nested_even_sum.nested_even_sum(obj2), 10)
        self.assertEqual(nested_even_sum.nested_even_sum(obj3), 0)
        self.assertEqual(nested_even_sum.nested_even_sum(obj4), 4)
        self.assertRaises(
            AssertionError, nested_even_sum.nested_even_sum, [("a", 3), ("b", 4)]
        )

    def test_capitalize_words(self):
        self.assertEqual(
            capitalize_words.capitalize_words(["i", "am", "learning", "recursion"]),
            ["I", "AM", "LEARNING", "RECURSION"],
        )
        self.assertEqual(
            capitalize_words.capitalize_words(["1", "2", "3", "4", "5"]),
            ["1", "2", "3", "4", "5"],
        )
        self.assertEqual(capitalize_words.capitalize_words([]), [])
        self.assertRaises(AssertionError, capitalize_words.capitalize_words, "1234")

    def test_stringify_numbers(self):
        obj1 = {
            "num": 1,
            "test": [],
            "data": {"val": 4, "info": {"isRight": True, "random": 66}},
        }
        obj2 = {"a": "nothing", "b": "hello"}
        self.assertEqual(
            stringify_numbers.stringify_numbers(obj1),
            {
                "num": "1",
                "test": [],
                "data": {"val": "4", "info": {"isRight": True, "random": "66"}},
            },
        )
        self.assertEqual(
            stringify_numbers.stringify_numbers(obj2), {"a": "nothing", "b": "hello"}
        )
        self.assertRaises(
            AssertionError, stringify_numbers.stringify_numbers, [("a", 3), ("b", 4)]
        )

    def test_collect_strings(self):
        obj1 = {
            "stuff": "foo",
            "data": {
                "val": {
                    "thing": {
                        "info": "bar",
                        "moreInfo": {"evenMoreInfo": {"weMadeIt": "baz"}},
                    }
                }
            },
        }
        obj2 = {"a": 1, "b": {"c": ["Hello"]}, "d": 3.17}
        self.assertEqual(collect_strings.collect_strings(obj1), ["foo", "bar", "baz"])
        self.assertEqual(collect_strings.collect_strings(obj2), [])
        self.assertRaises(
            AssertionError, collect_strings.collect_strings, [("a", 3), ("b", 4)]
        )

    def test_total_handshakes(self):
        self.assertEqual(total_handshakes.total_handshakes(25), (25 * 24) / 2)
        self.assertEqual(total_handshakes.total_handshakes(100), (100 * 99) / 2)
        self.assertEqual(total_handshakes.total_handshakes(1), 0)
        self.assertEqual(total_handshakes.total_handshakes(0), 0)
        self.assertRaises(AssertionError, total_handshakes.total_handshakes, "45")

    def test_total_diagonals(self):
        self.assertEqual(total_diagonals.total_diagonals(3), 0)
        self.assertEqual(total_diagonals.total_diagonals(4), 2)
        self.assertEqual(total_diagonals.total_diagonals(5), (5 * 2) / 2)
        self.assertEqual(total_diagonals.total_diagonals(6), (6 * 3) / 2)
        self.assertEqual(total_diagonals.total_diagonals(100), (100 * 97) / 2)
