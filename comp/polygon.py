#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

cuts = 0
cutting = True
if n == 1:
    if a[0] == 1:
        cuts = 3
    if a[0] == 2:
        cuts = 3
else:
    while cutting:
        cutting = False
        for i, ai in enumerate(a):
            if 2 * ai >= sum(a):
                cutting = True
                half1, half2 = ai // 2, ai - (ai // 2)
                cuts += 1
                a.pop(i)
                a.append(max(half1, half2))
                a.append(min(half2, half2))
print(cuts)
