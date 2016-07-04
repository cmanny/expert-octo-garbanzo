import sys
from functools import reduce
import operator

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        input()
        print(reduce(lambda x, y: (x * y) % 1234567, map(int, input().split()), 1))
