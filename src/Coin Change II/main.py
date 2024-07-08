class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount + 1):
                if i - coin < 0: continue
                dp[i] += dp[i - coin]
        return dp[amount]