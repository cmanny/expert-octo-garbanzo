import sys

def find(arr, m, i):
    for j in range(0, len(arr)):
        if arr[j] == m:
            return j

def ice_cream_parlour(arr, m):
    arr_set = set(arr)
    res = (-1, -1)
    for i in range(len(arr)):
        val = m - arr[i]
        if val in arr_set:
            j = find(arr, val, i)
            if i != j:
                return sorted([i + 1, j + 1])
    return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(" ".join(str(x) for x in ice_cream_parlour(arr, m)))
