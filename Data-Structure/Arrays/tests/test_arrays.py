import unittest
from Problems import (
    missing_num,
    two_sum,
    is_unique,
    permutation,
    rotate_matrix,
    subrectangle_queries,
    max_increase_to_keep_city_skyline,
)


class TestArrays(unittest.TestCase):
    def test_missing_num(self):
        self.assertEqual(missing_num.missing_num([1, 2, 3, 4, 5, 6, 8, 9, 10], 10), 7)
        self.assertEqual(missing_num.missing_num([], 0), 0)

    def test_two_sum(self):
        self.assertEqual(two_sum.two_sum_1([2, 6, 3, 9, 11], 9), [[6, 3]])
        self.assertEqual(two_sum.two_sum_2([2, 6, 3, 9, 11], 9), [[6, 3]])
        self.assertEqual(two_sum.two_sum_3([2, 6, 3, 9, 11], 9), [[6, 3]])
        self.assertEqual(two_sum.two_sum_1([2, 6, 5, 9, 11], 11), [[2, 9], [6, 5]])
        self.assertEqual(two_sum.two_sum_2([2, 6, 5, 9, 11], 11), [[2, 9], [6, 5]])
        self.assertEqual(
            two_sum.two_sum_3([2, 6, 5, 9, 11], 11), [[6, 5], [2, 9]]
        )  # order of elements list sequence will differ
        self.assertEqual(
            two_sum.two_sum_1([2, 6, 5, 9, 2, 11], 11), [[2, 9], [6, 5], [9, 2]]
        )
        self.assertEqual(
            two_sum.two_sum_2([2, 6, 5, 9, 2, 11], 11), [[2, 9], [6, 5], [9, 2]]
        )
        self.assertEqual(
            two_sum.two_sum_3([2, 6, 5, 9, 2, 11], 11), [[6, 5], [2, 9], [9, 2]]
        )
        self.assertEqual(two_sum.two_sum_1([2, 4, 3], 8), [])
        self.assertEqual(two_sum.two_sum_2([2, 4, 3], 8), [])
        self.assertEqual(two_sum.two_sum_3([2, 4, 3], 8), [])

    def test_is_unique(self):
        self.assertTrue(is_unique.is_unique([1, 2, 3, 4, 5, 6]))
        self.assertFalse(is_unique.is_unique([1, 2, 3, 4, 5, 1]))
        self.assertRaises(Exception, is_unique.is_unique, [])

    def test_permutation(self):
        self.assertTrue(permutation.permutation1(["a", "c", "d"], ["d", "a", "c"]))
        self.assertTrue(permutation.permutation2(["a", "c", "d"], ["d", "a", "c"]))
        self.assertTrue(permutation.permutation1([1, 2, 3, 5], [5, 3, 1, 2]))
        self.assertTrue(permutation.permutation2([1, 2, 3, 5], [5, 3, 1, 2]))
        self.assertFalse(permutation.permutation1(["a", "a", "b"], ["a", "b", "b"]))
        self.assertFalse(permutation.permutation2(["a", "a", "b"], ["a", "b", "b"]))
        self.assertFalse(
            permutation.permutation1(
                ["a", "a", "b", "c", "c", "c"], ["a", "b", "b", "b", "c", "c"]
            )
        )
        self.assertFalse(
            permutation.permutation2(
                ["a", "a", "b", "c", "c", "c"], ["a", "b", "b", "b", "c", "c"]
            )
        )

    def test_rotate_matrix(self):
        arr1 = [[1, 2], [3, 4]]
        arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr3 = []
        rotate_matrix.rotate_matrix(arr1)
        rotate_matrix.rotate_matrix(arr2)
        rotate_matrix.rotate_matrix(arr3)
        self.assertEqual(arr1, [[3, 1], [4, 2]])
        self.assertEqual(arr2, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
        self.assertEqual(arr3, arr3)
        self.assertRaises(
            Exception, rotate_matrix.rotate_matrix, [[1, 2], [3, 4], [4, 5, 6]]
        )

    def test_subrectangle_queries(self):
        rectangle1 = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
        answer1 = []
        obj1 = subrectangle_queries.SubRectangleQueries(rectangle1)
        answer1.append(obj1.get_value(0, 2))
        answer1.append(obj1.update_subrectangle(0, 0, 3, 2, 5))
        answer1.append(obj1.get_value(0, 2))
        answer1.append(obj1.get_value(3, 1))
        answer1.append(obj1.update_subrectangle(3, 0, 3, 2, 10))
        answer1.append(obj1.get_value(3, 1))
        answer1.append(obj1.get_value(0, 2))
        self.assertEqual(answer1, [1, None, 5, 5, None, 10, 5])

        rectangle2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        answer2 = []
        obj2 = subrectangle_queries.SubRectangleQueries(rectangle2)
        answer2.append(obj2.get_value(0, 0))
        answer2.append(obj2.update_subrectangle(0, 0, 2, 2, 100))
        answer2.append(obj2.get_value(0, 0))
        answer2.append(obj2.get_value(2, 2))
        answer2.append(obj2.update_subrectangle(1, 1, 2, 2, 20))
        answer2.append(obj2.get_value(2, 2))
        self.assertEqual(answer2, [1, None, 100, 100, None, 20])

    def test_max_increase_to_keep_city_skyline(self):
        grid1 = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        grid2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(
            max_increase_to_keep_city_skyline.max_increase_keeping_skyline(grid1),
            (35, [[8, 4, 8, 7], [7, 4, 7, 7], [9, 4, 8, 7], [3, 3, 3, 3]]),
        )
        self.assertEqual(
            max_increase_to_keep_city_skyline.max_increase_keeping_skyline(grid2),
            (0, grid2),
        )
