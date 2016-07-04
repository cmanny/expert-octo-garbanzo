import math

class SherlockMovingTiles(object):

    def __init__(self, l, s1, s2):
        self.l = l

        # Always assume s2 > s1
        if s1 > s2:
            self.s1, self.s2 = s2, s1
        else:
            self.s1, self.s2 = s1, s2

    def find_qi(self, qi):
        t = math.sqrt(2)*(math.sqrt(qi) - self.l)/(self.s1 - self.s2)
        return format(t, ".20f")


if __name__ == "__main__":
    smt = SherlockMovingTiles(*map(float, input().split()))
    n = int(input())
    for _ in range(n):
        print(smt.find_qi(float(input())))
