#!/bin/python3

import sys

def rewrite(i, j, grid):
    if (((i != len(grid) - 1) and grid[i + 1][j] < grid[i][j]) and \
        ((i != 0) and grid[i - 1][j] < grid[i][j]) and \
        ((j != len(grid) - 1) and grid[i][j + 1] < grid[i][j]) and \
        ((j != 0) and grid[i][j - 1] < grid[i][j])):
        return 'X'
    else: return grid[i][j]

if __name__ == "__main__":

    n = int(input().strip())
    grid = [[int(x) for x in input().strip()] for _ in range(n)]
    cavity_grid = [str(rewrite(i, j, grid)) + '\n' * (j == n - 1) for i in range(n) for j in range(n)]
    print("".join(cavity_grid))


