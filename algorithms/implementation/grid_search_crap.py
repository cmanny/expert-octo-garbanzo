#!/bin/python3

import sys

def match(G, i, j, P):
    return all(G[i + k][j : j + len(P[0])] == P[k] for k in range(len(P)))

def search(G, P):
    i = 0
    while i < len(G) - len(P) + 1:
        j = 0
        while j < len(G[0]) - len(P[0]) + 1:
            if(match(G, i, j, P)): 
                return True
            else: j += 1
        i += 1
    return False

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        R, C = [int(x) for x in input().strip().split(' ')]
        G = [str(input().strip()) for _ in range(R)]
        r, c = [int(x) for x in input().strip().split(' ')]
        P = [str(input().strip()) for _ in range(r)]
        print("YES" if search(G, P) else "NO")

