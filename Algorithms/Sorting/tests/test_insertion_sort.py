import unittest
from Problems.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_sorted_array(self):
        """Test already sorted array."""
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """Test reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        """Test an unsorted array."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        insertion_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_array_with_duplicates(self):
        """Test array containing duplicate elements."""
        arr = [4, 2, 4, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 2, 4, 4])

    def test_array_with_negative_numbers(self):
        """Test array with negative numbers."""
        arr = [3, -1, 0, -2, 5, 4]
        insertion_sort(arr)
        self.assertEqual(arr, [-2, -1, 0, 3, 4, 5])

    def test_single_element_array(self):
        """Test single element array."""
        arr = [42]
        insertion_sort(arr)
        self.assertEqual(arr, [42])

    def test_empty_array(self):
        """Test empty array."""
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])

    def test_reverse_parameter_true(self):
        """Test with reverse parameter set to True."""
        arr = [3, 1, 4, 2]
        insertion_sort(arr, reverse=True)
        self.assertEqual(arr, [4, 3, 2, 1])

    def test_reverse_sorted_array_with_reverse(self):
        """Test reverse parameter with reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr, reverse=True)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    def test_array_with_all_equal_elements(self):
        """Test array where all elements are equal."""
        arr = [7, 7, 7, 7, 7]
        insertion_sort(arr)
        self.assertEqual(arr, [7, 7, 7, 7, 7])
