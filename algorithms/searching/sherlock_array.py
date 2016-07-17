import sys

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        left_sum, right_sum = 0, sum(A)
        i = 1
        res = False or len(A) == 1
        while i < len(A):
            left_sum += A[i - 1]
            right_sum -= A[i - 1]
            if left_sum == right_sum - A[i]:
                res = True
            i += 1
        print("YES" if res else "NO")
