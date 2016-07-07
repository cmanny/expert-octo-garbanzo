import sys

def insertion(arr, printing=False):
    e = arr[-1]
    i = len(arr) - 2
    while i >= 0 and e < arr[i]:
        arr[i + 1] = arr[i]
        i -= 1
        if printing:
            print(" ".join([str(x) for x in arr]))
    arr[i + 1] = e
    if printing:
        print(" ".join([str(x) for x in arr]))
    return arr

if __name__ == "__main__":
    n = int(input())
    insertion([int(x) for x in input().split()], True)
