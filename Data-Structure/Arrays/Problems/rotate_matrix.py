# Write a function to rotate a N x N matrix by 90 degrees.


def rotate_matrix(arr):
    l = len(arr)
    for i in range(l):
        if len(arr[i]) != l:
            raise Exception("This is not NxN array")
    for x in range(l):
        for y in range(x + 1, l):
            arr[x][y], arr[y][x] = arr[y][x], arr[x][y]
    for x in range(l):
        for y in range(l // 2):
            arr[x][y], arr[x][-1 - y] = arr[x][-1 - y], arr[x][y]
