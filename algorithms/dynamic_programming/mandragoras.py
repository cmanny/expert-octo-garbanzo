import sys

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        H = [int(x) for x in input().split()]
        H_sorted = sorted(H)
        s = 1
        max_xp = 0
        H_sum = sum(H)
        for i in range(0, len(H)):
            max_xp = max(s * H_sum, max_xp)
            s += 1
            H_sum -= H_sorted[i]
        print(max_xp)
