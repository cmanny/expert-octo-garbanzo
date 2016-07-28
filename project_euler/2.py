import sys

def even_fib(N):
    a, b = 0, 1
    even_sum = 0
    if N < 2:
        return N
    else:
        while b < N:
            if b % 2 == 0:
                even_sum += b
            a, b = b, a + b
    return even_sum

t = int(input())

for _ in range(t):
    print(even_fib(int(input())))
