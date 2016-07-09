import sys

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition_swaps(arr, start, end, pivi):
    key = arr[pivi]
    pi = start
    swaps = 0
    for i in range(start, end):
        if arr[i] <= key:
            if pi != i:
                swap(arr, i, pi)
            swaps += 1
            pi += 1
    swaps += 1
    swap(arr, pi, pivi)
    return (swaps, pi)

def quicksort_swaps(arr, start, end):
    if start >= end:
        return 0
    swaps, p = partition_swaps(arr, start, end, end)
    swaps += quicksort_swaps(arr, start, p - 1)
    swaps += quicksort_swaps(arr, p + 1, end)
    return swaps

def insertion_swaps(arr):
    swaps = 0
    for j in range(1, len(arr)):
        i = j
        e = arr[j]
        while i > 0 and e < arr[i - 1]:
            arr[i] = arr[i - 1]
            swaps += 1
            i -= 1
        arr[i] = e
    return swaps

if __name__ == "__main__":
    t = int(input())
    arr_1 = [int(x) for x in input().split()]
    arr_2 = list(arr_1)
    print(insertion_swaps(arr_1) - quicksort_swaps(arr_2, 0, len(arr_2) - 1))
