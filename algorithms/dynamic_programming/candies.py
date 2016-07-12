import sys

if __name__ == "__main__":
    n = int(input())
    r = []
    candies = []
    for _ in range(n):
        r.append(int(input()))
        candies.append(1)
    for i in range(1, n):
        if r[i] > r[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(0, n - 1)[::-1]:
        if r[i] > r[i + 1]:
            if candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
    print(sum(candies))
