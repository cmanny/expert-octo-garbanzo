import sys

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, x = [int(x) for x in input().split()]
        if b < 0:
            _, a, _ = xgcd(a, x)
            b = -b
        print(pow(a, b, x))
