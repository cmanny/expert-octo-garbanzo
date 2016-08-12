import sys

def sub_sets(s):
    for i, t in enumerate(s):
        if t is 1:
            u[i] = x

n, m = [int(x) for x in input().split()]
u = [0 for _ in range(n)]
for _ in range(m):
    x = i = s = 0
    inp = [int(x) for x in input().split()]
    if int(inp[0]) != 3:
        i, x, s = [int(x) for x in inp]
    else:
        i, s = [int(x) for x in inp]
        
    s = [int(x) for x in str(s)]
    if i == 1:
    elif i == 2:
        for i, t in enumerate(s):
            if t is 1:
                u[i] ^= x   
    elif i == 3:
        for i, t in enumerate(s):
            if t is 1:
                print(u[i])
