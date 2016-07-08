import sys

def partition(arr, pivot):
    pivot = arr[pivot]
    left, equal, right = [], [], []
    for x in arr:
        partition = equal if x == pivot else (left if x < pivot else right)
        partition.append(x)
    return (left, equal, right)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    left, equal, right = partition(arr, 0)
    res = quicksort(left) + equal + quicksort(right)
    print(" ".join(str(x) for x in res))
    return res

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    quicksort(arr)

