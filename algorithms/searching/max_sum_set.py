import sys

q = int(input())
for _ in range(q):
    n, m = [int(x) for x in input().split()]
    a_arr = [int(x) % m  for x in input().split()]
    for i in range(1, len(a_arr)):
        a_arr[i] = (a_arr[i - 1] + a_arr[i]) % m
    a_arr = sorted([(x, i) for i, x in enumerate(a_arr)], key = lambda x: x[0])
    max_sum = a_arr[0][0]
    for i in range(0, len(a_arr) - 1):
        if (a_arr[i][1] > a_arr[i + 1][1] and a_arr[i][0] < a_arr[i + 1][0]):
            max_sum = max(max_sum, (a_arr[i][0] - a_arr[i + 1][0]) % m)
    print(max(max_sum, a_arr[-1][0]))
    
