def heap_sort(arr, reverse=False):
    def heapify(arr, l, i, reverse):
        compare = lambda x, y: x < y if reverse else x > y

        # Initialize largest as root
        largest = i

        left = 2 * i + 1  # left = 2*i + 1
        right = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is greater than root
        if left < l and compare(arr[left], arr[largest]):
            largest = left

        # See if right child of root exists and is greater than root
        if right < l and compare(arr[right], arr[largest]):
            largest = right

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            # heapify the root
            heapify(arr, l, largest, reverse)

    # step 1: build heap
    l = len(arr)
    for i in range(
        (l // 2) - 1, -1, -1
    ):  # (l//2)-1 ensures that we are not starting from leaf nodes
        heapify(arr, l, i, reverse)

    # step 2: extract the root and heapify the remaining tree
    for i in range(l - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, reverse)
