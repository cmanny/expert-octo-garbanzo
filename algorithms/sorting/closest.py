import sys


if __name__ == "__main__":
    n = int(input())
    A = [int(x) for x in input().split()]
    A = sorted(A)
    min_dist = min(abs(A[i] - A[i - 1]) for i in range(1, len(A)) if A[i] != A[i - 1])
    out = []
    for i in range(1, len(A)):
        if abs(A[i] - A[i - 1]) == min_dist:
            out.append(A[i - 1])
            out.append(A[i])
    print(" ".join(str(x) for x in out))
