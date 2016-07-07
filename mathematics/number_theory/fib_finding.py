import sys
import math
import copy

def mat_mul(mat1, mat2, mod):
    ret_mat = [[0, 0], [0, 0]]
    ret_mat[0][0] = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % mod
    ret_mat[0][1] = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % mod
    ret_mat[1][0] = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % mod
    ret_mat[1][1] = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % mod
    return ret_mat

def mat_pow(mat, n, mod):
    res = [[1, 0], [0, 1]]
    while n > 1:
        if n & 1:
            res = mat_mul(res, mat, mod)
        res = mat_mul(res, res, mod)
        n >>= 1
    return res

if __name__  == "__main__":
    phi = (1 + 5 ** 0.5) / 2
    t = int(input())
    for _ in range(t):
        a, b, n = [int(x) for x in input().split()]
        mat = [[1, 1], [1, 0]]
        res = mat_pow(mat, n, 10**9 + 7)
        print(res[1][0] * b + res[1][1] * a)
    
