"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

DENOMINATIONS = [1, 5, 10, 25]


# This problem will run very slowly! Time: (O(2n))
def minimum_coins(n):
    if n == 0:
        return 0
    elif n in DENOMINATIONS:
        return 1
    else:
        return min(1 + minimum_coins(n - d) for d in DENOMINATIONS if n - d >= 0)


# Improvement on the solution using dynamic programming
def minimum_coins_dp(n):
    cache = [0 for _ in range(n + 1)]

    for d in DENOMINATIONS:
        if d < len(cache):
            cache[d] = 1

    for i in range(1, n + 1):
        cache[i] = min(1 + cache[i - d] for d in DENOMINATIONS if i - d >= 0)

    return cache[n]
