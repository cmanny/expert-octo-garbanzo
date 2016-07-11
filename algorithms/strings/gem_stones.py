import sys

def gem_stones(stones):
    stones_sets = [set(s) for s in stones]
    gem_set = set.intersection(*stones_sets)
    return gem_set

if __name__ == "__main__":
    n = int(input())
    stones = []
    for _ in range(n):
        stones.append(list(input().strip()))
    print(len(gem_stones(stones)))
