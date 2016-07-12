import sys
import string

def alph_counter(chars):
    counts = dict()
    for i in string.ascii_lowercase:
        counts[i] = 0
    for x in chars:
        counts[x] += 1
    return counts

if __name__ == "__main__":
    s1 = alph_counter(input().strip())
    s2 = alph_counter(input().strip())
    diff = 0
    for x in string.ascii_lowercase:
        diff += abs(s1[x] - s2[x])
    print(diff)
