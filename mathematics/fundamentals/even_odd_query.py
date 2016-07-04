import sys

def find(arr, x, y):
    if x > y: return 1
    return arr[x] ** find(arr, x + 1, y)

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    q = int(input())
    for _ in range(q):
        x, y = map(lambda x: int(x) - 1, input().split())
        if x != y:
            out = "Odd" if (arr[x] % 2 == 1 or x > y or (x + 1 < n and arr[x + 1] == 0)) else "Even"
        else:
            out = "Odd" if arr[x] % 2 == 1 else "Even"
        print(out)
