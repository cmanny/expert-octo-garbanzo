import sys

def how_many(x, N):
    count = (N // x)
    return x * count * (count + 1) // 2

t = int(input())

for _ in range(t):
    n = int(input()) - 1
    print(how_many(3, n) + how_many(5, n) - how_many(15, n))
