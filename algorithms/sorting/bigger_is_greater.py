import sys


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def next_largest_perm(string):
    if len(string) == 1:
        return string
    seqi = len(string) - 1
    while seqi > 0 and string[seqi - 1] >= string[seqi]:
        seqi -= 1
    if seqi <= 0:
        return string
    seqi -= 1
    swapi = len(string) - 1
    while string[swapi] <= string[seqi]:
        swapi -= 1
    swap(string, swapi, seqi)
    string = string[0:seqi + 1] + string[len(string) - 1:seqi:-1]
    return string



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        instr = input().strip()
        outstr = "".join(next_largest_perm([x for x in instr]))
        if instr == outstr:
            print("no answer")
        else:
            print(outstr)
