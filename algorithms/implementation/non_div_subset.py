import sys
from collections import Counter

if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    counter = Counter([int(x) % k for x in input().split()])
    size = 0
    for key in range(k // 2 + 1):
        if key in counter or k - key in counter:
            v = counter[key]
            if k == key * 2 or key == 0: size += 1
            elif k - key in counter:
                size += max(v, counter[k - key])
            else:
                size += v
    print(size)





