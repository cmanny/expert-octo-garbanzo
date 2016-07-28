import sys
import math

root_n  = int(math.sqrt(10**7) + 1)

num_divs = [1 for x in range(10**7 + 1)] 
antiprimes = []

cur_max_divs = 1
for i in range(2, 10**8):
    for j in range(i, 10**8, i):
        num_divs[j] += 1
    if num_divs[i] > cur_max_divs:
        cur_max_divs = num_divs[i]
        antiprimes += [i]

print(antiprimes)
