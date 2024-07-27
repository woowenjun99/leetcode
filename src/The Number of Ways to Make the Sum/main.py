class Solution:
    def numberOfWays(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        if n >= 4: dp[4] += 1
        if n >= 8: dp[8] += 1
        coins = [1, 2, 6]

        for coin in coins:
            for a in range(n + 1):
                if a - coin < 0: continue
                dp[a] += dp[a - coin]
        return dp[-1] % (10**9 + 7)
