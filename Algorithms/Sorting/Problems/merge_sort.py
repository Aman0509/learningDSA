def merge_sort(arr, reverse=False):
    """
    Out of place and Stable Sorting method
    TC - O(nlogn)
    SC - O(n)
    """
    compare = lambda x, y: x < y if reverse else x > y
    l = len(arr)
    if l > 1:
        mid = l // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr, reverse)
        merge_sort(right_arr, reverse)
        i = j = k = 0
        l1 = len(left_arr)
        l2 = len(right_arr)
        while i < l1 and j < l2:
            if compare(right_arr[j], left_arr[i]):
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < l1:
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < l2:
            arr[k] = right_arr[j]
            j += 1
            k += 1
