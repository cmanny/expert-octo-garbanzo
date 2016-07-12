import sys

# also known as, nikita an the game
def sum_between(A, x, y):
    if x == 0:
        return A[y]
    else:
        return A[y] - A[x - 1]

def _splitting_game(A, x, y):
    i = x
    while i <= y and sum_between(A, x, i) != sum_between(A, i + 1, y):
        i += 1
    if i == x and A[x] == 0:
        return len(A) - 1
    #no split found
    if i >= y + 1:
        return 0
    else:
        return 1 + max(_splitting_game(A, x, i), _splitting_game(A, i + 1, y))


def splitting_game(A):
    sums = [x for x in A]
    for i in range(1, len(A)):
        sums[i] += sums[i - 1]
    return _splitting_game(sums, 0, len(A) - 1)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        print(splitting_game(A))
