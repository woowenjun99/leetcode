from typing import List

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        dp = [float("inf")] * (len(target) + 1)
        dp[-1] = 0
        for i in range(len(target) - 1, -1, -1):
            for word, cost in zip(words, costs):
                if i + len(word) > len(target) or target[i: len(word) + i] != word: continue
                dp[i] = min(dp[i], cost + dp[len(word) + i])
        return dp[0] if dp[0] != float("inf") else -1