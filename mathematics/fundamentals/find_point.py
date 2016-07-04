import sys

def find_point(px, py, qx, qy):
   return (2*qx - px, 2*qy - py)

if __name__ == "__main__":
    for line in sys.stdin:
        print(find_point(*map(int, line.split())))
