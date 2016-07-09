import sys

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition_in_place(arr, start, end, pivi):
    key = arr[pivi]
    pi = start
    for i in range(start, end):
        if arr[i] <= key:
            if pi != i:
                swap(arr, i, pi)
            pi += 1
    swap(arr, pi, pivi)
    return pi

def quicksort(arr, start, end):
    if start >= end:
        return arr
    p = partition_in_place(arr, start, end, end)
    print(" ".join(str(x) for x in arr))
    quicksort(arr, start, p - 1)
    quicksort(arr, p + 1, end)
    return arr

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    quicksort(arr, 0, len(arr) - 1)

