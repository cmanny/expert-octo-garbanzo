import sys

def alternating_chars(string):
    ndel = 0
    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            ndel += 1
    return ndel


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(alternating_chars(input().strip()))
