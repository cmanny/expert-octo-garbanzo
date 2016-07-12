import sys

def max_subarray(A):
    contiguous_max = best_max = A[0]
    for x in A[1:]:
        contiguous_max = max(x, contiguous_max + x)
        best_max = max(best_max, contiguous_max)
    return best_max

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        contiguous_max = max_subarray(A)
        noncontig_max = sum(x for x in A if x > 0)
        if noncontig_max == 0:
            noncontig_max = max(A)
        print(" ".join(str(x) for x in [contiguous_max, noncontig_max]))
