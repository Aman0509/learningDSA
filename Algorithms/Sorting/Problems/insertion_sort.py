def insertion_sort(arr, reverse=False):
    """
    In place and Stable Sorting method
    TC - O(n^2)
    SC - O(1)
    """
    compare = lambda x, y: x < y if reverse else x > y
    l = len(arr)
    for i in range(1, l):
        key = arr[i]
        idx = i - 1
        while idx >= 0 and compare(arr[idx], key):
            arr[idx + 1] = arr[idx]
            idx -= 1
        arr[idx + 1] = key
