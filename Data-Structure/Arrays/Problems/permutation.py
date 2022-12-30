# Write a function which accepts 2 lists to find if both are permutation of each other.


def permutation1(arr1, arr2):
    if len(arr1) == len(arr2):
        d = {}
        for i in arr1:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        for j in arr2:
            if j in d:
                d[j] -= 1
                if d[j] < 0:
                    return False
        return True


def permutation2(arr1, arr2):
    if len(arr1) == len(arr2):
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        if arr1 == arr2:
            return True
    return False
