import sys

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def find_partition(arr, start, end, pivi):
    key = arr[pivi]
    pi = start
    for i in range(start, end):
        if arr[i] <= key:
            if pi != i:
                swap(arr, i, pi)
            pi += 1
    swap(arr, pi, pivi)
    return pi

def quickselect(arr, start, end, n):
    if start == end:
        return arr[start]

    piv = find_partition(arr, start, end, end)
    if piv == n:
        return arr[n]
    elif piv > n:
        return quickselect(arr, start, piv - 1, n)
    else:
        return quickselect(arr, piv + 1, end, n)

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(quickselect(arr, 0, n - 1, n // 2))
