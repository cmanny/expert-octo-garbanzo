import sys

if __name__ == "__main__":
    s = list(input().strip())
    res = []
    for c in s:
        if res and res[-1] == c:
            del res[-1]
        else:
            res += c
    print("Empty String" if not res else "".join(res))
        
        
