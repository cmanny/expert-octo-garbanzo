import sys

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, i = map(int, input().split())
        if i < int(n/2):
            print(2*i + 1)
        else:
            print(int(2*(n - 1 - i)))
