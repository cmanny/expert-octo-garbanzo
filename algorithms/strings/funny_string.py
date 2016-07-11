import sys

def is_funny(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if abs(s[i] - s[i - 1]) != abs(s[n - i] - s[n - i - 1]):
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print("Funny" if is_funny([ord(a) for a in input().strip()]) else "Not Funny")
