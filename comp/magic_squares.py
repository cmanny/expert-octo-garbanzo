import sys

import itertools

magic_squares = []

def is_magic_square(m):
    for j in range(3):
        if sum(m[j]) != 15: return False
    for i in range(3):
        if sum([m[0][i] + m[1][i] + m[2][i]]) != 15: return False
    if sum([m[0][0] + m[1][1] + m[2][2]]) != 15: return False
    if sum([m[0][2] + m[1][1] + m[2][0]]) != 15: return False
    return True

for x in itertools.permutations(range(1,10)):
    m = [x[0:3], x[3:6], x[6:9]]
    if is_magic_square(m):
        magic_squares.append([x for x in itertools.chain.from_iterable(m)])
print("\n".join(str(x) for x in magic_squares))
