#!/bin/python3

import sys

if __name__ == "__main__":
    T = int(input())
    for a0 in range(T):
        n = int(input())
        q = [int(qi) for qi in input().split()]
        if any((qi - 1 - i) > 2 for i, qi in enumerate(q)):
            print("Too chaotic")
        else:
            print(sum(1 for i in range(len(q) - 1, -1, -1) \
                    for j in range(max(0, q[i] - 2), i) if q[j] > q[i]))
            

