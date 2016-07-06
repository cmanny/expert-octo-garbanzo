import sys


if __name__ == "__main__":
    n1,n2,n3 = [int(x) for x in input().split()]
    h1 = [int(x) for x in input().split()]
    h2 = [int(x) for x in input().split()]
    h3 = [int(x) for x in input().split()]
    stacks = [h1, h2, h3]
    heights = [sum(h1), sum(h2), sum(h3)]
    while len(set(heights)) > 1:
        i = max(range(0,3), key = lambda x: heights[x])
        heights[i] -= stacks[i].pop(0)
    print(heights[0])
    
