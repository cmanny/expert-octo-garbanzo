import sys

def partition(arr, pivot):
    pivot = arr[pivot]
    left, equal, right = [], [], []
    for x in arr:
        partition = equal if x == pivot else (left if x < pivot else right)
        partition.append(x)
    return (left, equal, right)
if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(" ".join(str(x) for y in partition(arr, 0) for x in y))

