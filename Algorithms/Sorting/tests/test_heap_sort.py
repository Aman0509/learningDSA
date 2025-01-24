import unittest
from Problems.heap_sort import heap_sort


class TestHeapSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_flag(self):
        arr = [1, 2, 3, 4, 5]
        heap_sort(arr, reverse=True)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    def test_duplicates(self):
        arr = [4, 1, 3, 2, 2, 4, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 2, 3, 4, 4])

    def test_empty_array(self):
        arr = []
        heap_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [42]
        heap_sort(arr)
        self.assertEqual(arr, [42])

    def test_large_numbers(self):
        arr = [999999999, 1, 500, 123456789]
        heap_sort(arr)
        self.assertEqual(arr, [1, 500, 123456789, 999999999])

    def test_negative_numbers(self):
        arr = [-1, -3, -2, -5, 0]
        heap_sort(arr)
        self.assertEqual(arr, [-5, -3, -2, -1, 0])
