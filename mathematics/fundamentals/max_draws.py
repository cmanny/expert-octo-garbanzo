import sys

if __name__ == "__main__":
    n = int(input())
    if n is 0:
        print(0)
    else:
        for _ in range(n):
            print(str(int(input())+1))
