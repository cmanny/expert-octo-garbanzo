import sys

def can_move(a, b, x, y):
    if b == 0:
        if x != a: 
            return False
    elif (x - a) % b != 0:
        return False
    if a == 0:
        if y != b: 
            return False
    elif (y - b) % a != 0:
        return False
    return True

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        print("YES" if can_move(*map(int, input().split())) else "NO")
