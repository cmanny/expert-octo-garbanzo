import sys
from collections import Counter

if __name__ == "__main__":
    n = int(input())
    arr1 = Counter([int(x) for x in input().split()])
    m = int(input())
    arr2 = Counter([int(x) for x in input().split()])
    arr1.subtract(arr2)
    print(" ".join(sorted([str(k) for k, v in arr1.items() if v != 0])))
