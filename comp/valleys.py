import sys

n = int(input())
height_arr = [1 if x == "U" else -1 for x in input()]
height, last_height = 0, 0
num_valleys = 0
for x in height_arr:
    last_height, height = height, height + x
    if height == 0 and last_height < 0:
        num_valleys += 1
print(num_valleys)
