import sys
import string


def alph_counter(chars):
    counts = dict()
    for i in string.ascii_lowercase:
        counts[i] = 0
    for x in chars:
        counts[x] += 1
    return counts

def game_of_thrones(string):
    counts = alph_counter(s)
    l = len(s)
    found_odd = False
    for k, v in counts.items():
        if v & 1:
            if not l & 1:
                return False
            if found_odd:
                return False
            else:
                found_odd = True
    return True





if __name__ == "__main__":
    s = input().strip()
    print("YES" if game_of_thrones(s) else "NO")
