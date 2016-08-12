import sys


n, m = [int(x) for x in input().split()]
queries = []

for mi in range(m):
    x = i = s = 0
    inp = [int(x) for x in input().split()]
    if int(inp[0]) != 3:
        i, x, s = [int(x) for x in inp]
        queries.append((i, x, int(str(s), 2)))
    else:
        i, s = [int(x) for x in inp]
    s = int(str(s), 2)
    val = 0
    start = 0
    if i == 3:
        for j in range(len(queries) - 1, -1, -1):
            q = queries[j]
            if q[2] & s == s and q[0] == 1:
                start = j
                break
        
        for qi in range(start, len(queries)):
            q = queries[qi]
            # if is a subset
            if s & q[2] == s: 
                if q[0] == 1:
                    val = q[1]
                elif q[0] == 2:
                    val ^= q[1]
        print(val)
                
