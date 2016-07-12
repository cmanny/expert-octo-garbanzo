import sys

def coin_change(n, coins, memo, coin_i):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if coin_i < 0:
        return 0
    if memo[n][coin_i] != -1:
        return memo[n][coin_i]
    memo[n][coin_i] = coin_change(n, coins, memo, coin_i - 1) + \
                        coin_change(n - coins[coin_i], coins, memo, coin_i)
    return memo[n][coin_i]

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    coins = [int(x) for x in input().split()]
    memo = [[-1 for _ in coins] for _ in range(n + 1)]
    print(coin_change(n, coins, memo, m - 1))
