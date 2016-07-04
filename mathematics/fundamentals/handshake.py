import sys
import math

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        h = int(input())
        print(int(h * (h - 1) / 2))
