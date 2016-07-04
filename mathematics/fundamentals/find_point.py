import sys

def find_point(px, py, qx, qy):
   return (2*qx - px, 2*qy - py)

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        print(" ".join(map(str, find_point(*map(int, input().split())))))
