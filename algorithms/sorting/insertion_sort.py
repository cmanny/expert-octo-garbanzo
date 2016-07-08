import sys

def insertion(arr, start, printing=False):
    e = arr[start]
    i = start
    while i > 0 and e < arr[i - 1]:
        arr[i] = arr[i - 1]
        i -= 1
    arr[i] = e
    if printing:
        print(" ".join([str(x) for x in arr]))
    return arr

if __name__ == "__main__":
    s = int(input())
    arr = [int(x) for x in input().split()]
    for i in range(1, s):
        arr = insertion(arr, i, True)

