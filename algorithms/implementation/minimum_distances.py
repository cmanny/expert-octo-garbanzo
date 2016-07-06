#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input().strip())
    A = [int(A_temp) for A_temp in input().strip().split(' ')]
    try:
        print(min(abs(i - j) for i in range(len(A)) \
                for j in range(i + 1, len(A)) if A[i] == A[j]))
    except ValueError:
        print(-1)
