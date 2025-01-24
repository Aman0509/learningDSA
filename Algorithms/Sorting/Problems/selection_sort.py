def selection_sort(arr, reverse=False):
    """
    In place and Unstable Sorting method
    TC - O(n^2)
    SC - O(1)
    """
    compare = lambda x, y: x < y if reverse else x > y
    l = len(arr)
    for i in range(l):
        idx = i
        for j in range(i+1, l):
            if compare(arr[idx], arr[j]):
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
