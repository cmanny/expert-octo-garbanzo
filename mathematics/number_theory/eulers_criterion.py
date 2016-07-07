import sys

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, m = [int(x) for x in input().split()]
        print("YES" if pow(a, int((m - 1) / 2), m) == 1 or a == 0 else "NO")
