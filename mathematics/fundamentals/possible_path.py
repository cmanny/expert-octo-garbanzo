import sys

def can_move(a, b, x, y):
    if b == 0:
        if x != a or y != b: 
            return False
    else:
        if (x - a) % b != 0:
            return False
        if (y - a) % b != 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        print("YES" if can_move(*map(int, input().split())) else "NO")
