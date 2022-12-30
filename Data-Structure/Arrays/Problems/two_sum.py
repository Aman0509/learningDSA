# Write a program to find all the pairs of integers whose sum is equal to a given number


# Brute Force
def two_sum_1(arr, num):
    l = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = num - arr[i]
            if arr[j] == diff:
                l.append([arr[i], arr[j]])
    return l


# Two-pass Hash Table
def two_sum_2(arr, num):
    hashmap = {}
    l = []
    for i in range(len(arr)):
        if hashmap.get(arr[i]):
            hashmap[arr[i]].append(i)
        else:
            hashmap[arr[i]] = [i]
    for i in range(len(arr)):
        complement = num - arr[i]
        if (
            complement in hashmap
            and len(hashmap[complement]) != 0
            and hashmap[complement][0] != i
        ):
            l.append([arr[i], arr[hashmap[complement][0]]])
            hashmap[arr[i]].pop(0)
    return l


# One-pass hash table
def two_sum_3(arr, num):
    hashmap = {}
    l = []
    for i in range(len(arr)):
        complement = num - arr[i]
        if complement in hashmap:
            l.append([arr[hashmap.get(complement)], arr[i]])
        hashmap[arr[i]] = i
    return l
