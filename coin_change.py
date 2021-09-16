"""
You are given an integer array coins representing coins of different denominations and an
integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of
money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2
"""


# Using Dynamic Programming
def coin_change(coins, amount):
    if not amount:
        return 0

    dp = [float("inf") for i in range(amount + 1)]

    for i in range(1, amount + 1):
        if i in coins:
            dp[i] = 1
        else:
            new = [coin for coin in coins if coin < i]
            if not new:
                dp[i] = float("inf")
            for j in new:
                dp[i] = min(dp[i], 1 + dp[i - j])
    if dp[-1] == float("inf"):
        return -1

    return dp[-1]


# -------------------------Using BFS-------------------------

def coin_change_bfs(self, coins, amount):
    if amount == 0:
        return 0

    curr_queue = [0]
    next_queue = []
    visited = [False] * (amount + 1)
    level = 1
    while curr_queue:
        curr = curr_queue.pop()

        for c in coins:
            child = curr + c

            if child == amount:
                return level

            if child > amount:
                continue

            if not visited[child]:
                next_queue.append(child)
                visited[child] = True

        if not curr_queue:
            level += 1
            curr_queue, next_queue = next_queue, curr_queue

    return -1
