from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        for i in range(1, len(cost)): cost[i] = min(cost[i - 1], cost[i])
        return cost
