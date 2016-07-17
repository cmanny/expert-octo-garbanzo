import sys
import math

def dict_counter(n, nums):
    counts = dict()
    for x in nums:
        try:
            counts[x] += 1
        except KeyError:
            counts[x] = 1
    return counts

def nCk(n, k):
    if k > n: return 0
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        counts = dict_counter(n, A)
        print(sum(2 * nCk(v, 2) for k, v in counts.items()))
