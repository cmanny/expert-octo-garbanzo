import sys

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s1, s2 = input().strip(), input().strip()
        print("YES" if len(set.intersection(set(s1), set(s2))) > 0 else "NO")
