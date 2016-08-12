import sys
import math
from collections import Counter

n = int(input())
arr = [0] + [int(x) for x in input().split()]
data_arr = [[None, None] for _ in range(n + 1)]
primes = [Counter() for _ in range(n + 1)]


def compute():
    num = 1
    for i in range(2, n + 1):
        # if prime
        if len(primes[i]) == 0:
            pow_i = 1
            inc = i
            while inc <= n + 1:
                cur_pow = i**pow_i
                if cur_pow > n:
                    break
                inc = cur_pow
                if arr[inc] == -1:
                    data_arr[inc] = [i, None]
                else:
                    data_arr[inc] = [1, arr[inc]]
                print(data_arr[inc])
                for j in range(inc + inc, n + 1, inc):
                    if data_arr[j][0] == None:
                        data_arr[j][0] = 1
                    if arr[j] != -1:
                        if data_arr[cur_pow][1] == None:
                            data_arr[cur_pow][0] = 1
                            data_arr[cur_pow][1] = arr[j] % cur_pow
                        else:
                            if data_arr[cur_pow][1] != arr[j] % cur_pow:
                                #bad sequence, abort
                                return 0
                    #for all composites
                    primes[j] = primes[j] + Counter({i : 1})
                pow_i = pow_i + 1
    for i in range(2, n + 1):
        num *= data_arr[i][0]
    return num

            
print(compute())
