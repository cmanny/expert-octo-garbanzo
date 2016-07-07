import sys

def counter(n, nums):
    counts = dict()
    for i in range(n):
        counts[i] = 0
    for x in nums:
        counts[x] += 1
    return counts

if __name__ == "__main__":
    t = int(input())
    print(" ".join(str(v) for k, v in counter(n, [int(x) for x in input().split()]).items()))
