import sys
import math

def gen_divisors(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            if n != i*i: yield int(n / i)
    return None

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(len([d for d in gen_divisors(int(input())) if d & 1 == 0]))
