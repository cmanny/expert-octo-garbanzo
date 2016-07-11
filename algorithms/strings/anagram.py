import sys
import string

def alph_counter(chars):
    counts = dict()
    for i in string.ascii_lowercase:
        counts[i] = 0
    for x in chars:
        counts[x] += 1
    return counts


def changes_needed(s1, s2):
    change = 0
    for x in string.ascii_lowercase:
        change += abs(s1[x] - s2[x])
    return change // 2

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        l = len(s)
        if l & 1:
            print(-1)
        else:
            print(changes_needed(alph_counter(s[0:l // 2]), alph_counter(s[l // 2:l])))
