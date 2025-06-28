from typing import List

class Solution:
    def __coin_change_two(self, coins: List[int], amount: int) -> int:
        old = [0] * (amount + 1)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for index in range(len(dp)):
                if index - coin < 0: continue
                dp[index] = old[index] + dp[index - coin]
            old = dp.copy()
        return dp[-1]

    def findCoins(self, numWays: List[int]) -> List[int]:
        coins = []
        for amount, numWay in enumerate(numWays):
            coins.append(amount + 1)
            if self.__coin_change_two(coins, amount + 1) == numWay: continue
            coins.pop()
            if self.__coin_change_two(coins, amount + 1) == numWay: continue
            return []
        return coins
