import sys

def plug_string(string):
    retstr = ""
    i = num_changes = 0
    while i <= len(string) - 3:
        if string[i:i + 3] == "010":
            retstr += "011"
            num_changes += 1
            i += 3
        else:
            retstr += string[i]
            i += 1
    return (retstr, num_changes)

if __name__ == "__main__":
    n = int(input())
    bstring = input().strip()
    print(plug_string(bstring)[1])
