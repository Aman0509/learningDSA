import unittest
from Problems.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_sorted_array(self):
        """Test already sorted array."""
        arr = [1, 2, 3, 4, 5]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """Test reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        """Test unsorted array."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        quick_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_array_with_duplicates(self):
        """Test array with duplicate elements."""
        arr = [4, 2, 4, 2, 1]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 2, 4, 4])

    def test_array_with_negative_numbers(self):
        """Test array with negative numbers."""
        arr = [3, -1, 0, -2, 5, 4]
        quick_sort(arr)
        self.assertEqual(arr, [-2, -1, 0, 3, 4, 5])

    def test_single_element_array(self):
        """Test single element array."""
        arr = [42]
        quick_sort(arr)
        self.assertEqual(arr, [42])

    def test_empty_array(self):
        """Test empty array."""
        arr = []
        quick_sort(arr)
        self.assertEqual(arr, [])

    def test_reverse_parameter_true(self):
        """Test reverse sorting with reverse parameter."""
        arr = [3, 1, 4, 2]
        quick_sort(arr, reverse=True)
        self.assertEqual(arr, [4, 3, 2, 1])

    def test_reverse_sorted_array_with_reverse(self):
        """Test reverse sorted array with reverse parameter."""
        arr = [5, 4, 3, 2, 1]
        quick_sort(arr, reverse=True)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    def test_array_with_all_equal_elements(self):
        """Test array where all elements are equal."""
        arr = [7, 7, 7, 7, 7]
        quick_sort(arr)
        self.assertEqual(arr, [7, 7, 7, 7, 7])

    def test_large_array(self):
        """Test large array with same elements."""
        arr = [100] * 200  # 200 elements, all equal
        quick_sort(arr)
        self.assertEqual(arr, [100] * 200)  # Should remain unchanged

    def test_reverse_parameter_on_empty_array(self):
        """Test reverse parameter on empty array."""
        arr = []
        quick_sort(arr, reverse=True)
        self.assertEqual(arr, [])

    def test_reverse_sorted_array_with_reverse_parameter(self):
        """Test reverse sorted array with reverse=True."""
        arr = [10, 9, 8, 7, 6]
        quick_sort(arr, reverse=True)
        self.assertEqual(arr, [10, 9, 8, 7, 6])

    def test_reverse_array_with_reverse_parameter(self):
        """Test reverse array with reverse=True."""
        arr = [6, 7, 8, 9, 10]
        quick_sort(arr, reverse=True)
        self.assertEqual(arr, [10, 9, 8, 7, 6])
