import sys

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c = [int(x) for x in input().split()]
        div = round((a ** b) / c)
        print(div * c)
