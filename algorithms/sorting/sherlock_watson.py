import sys

if __name__ == "__main__":
    n, k, q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    for _ in range(q):
        print(arr[(int(input()) - k) % n])
