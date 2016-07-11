import sys

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        string = input().strip()
        changes = 0
        for i in range(0, len(string) // 2):
            changes += abs(ord(string[i]) - ord(string[len(string) - i - 1]))
        print(changes)
