import fractions

def can_move(a, b, x, y):
    return fractions.gcd(x,y) == fractions.gcd(a,b)

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        print("YES" if can_move(*map(int, input().split())) else "NO")
