import sys

if __name__ == "__main__":
    n = int(input().strip())
    h = [int(x) for x in input().split()]
    while(len(h) > 0):
        print(len(h))
        minh = min(h)
        h = [(x - minh) for x in h if (x - minh)]
