import sys

class NCRTable(object):

    def __init__(self, depth=2000, mod=10**9):
        self.depth = depth
        self.table = []
        self.mod = mod
        self.generate()

    def generate(self):
        self.table.append([])
        self.table.append([1,1])
        for i in range(2, self.depth):
            self.table.append([1] + \
                    [(self.table[i-1][x-1] + self.table[i-1][x]) % self.mod for x in range(1, len(self.table[i-1]))] \
                    + [1])

    def choose(self, n, r):
        return self.table[n][r]

    def row(self, n):
        return self.table[n]

if __name__ == "__main__":
    t = int(input())
    table = NCRTable();
    for _ in range(t):
        print(" ".join(map(str, table.row(int(input())))))
    
