def quick_sort(arr, reverse=False):
    """
    In place and Unstable Sorting method
    TC - O(n log n) on average, O(n^2) in the worst case
    SC - O(log n) on average (for recursion stack)
    """

    def partition(arr, low, high, reverse):
        compare = lambda x, y: x < y if reverse else x > y
        piv = arr[high]
        i = low - 1
        for j in range(low, high):
            if compare(piv, arr[j]):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high, reverse):
        if low < high:
            piv = partition(arr, low, high, reverse)
            quick_sort_recursive(arr, low, piv - 1, reverse)
            quick_sort_recursive(arr, piv + 1, high, reverse)

    quick_sort_recursive(arr, 0, len(arr) - 1, reverse)
