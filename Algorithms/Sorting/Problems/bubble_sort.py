def bubble_sort(arr, reverse=False):
    """
    In place and Stable Sorting method
    TC - O(n^2)
    SC - O(1)
    """
    compare = lambda x, y: x < y if reverse else x > y
    l = len(arr)
    for i in range(l):
        for j in range(l - i - 1):
            if compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
