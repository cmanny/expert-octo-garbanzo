import sys
import fractions



if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        b, l = map(int, input().split())
        print(int(b*l/fractions.gcd(b, l)**2))
