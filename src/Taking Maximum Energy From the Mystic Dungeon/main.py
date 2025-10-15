from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        answer = float("-inf")
        for i in range(len(energy) - 1, -1, -1):
            dp[i] += energy[i]
            if i - k >= 0: dp[i - k] = dp[i]
            answer = max(answer, dp[i])
        return answer