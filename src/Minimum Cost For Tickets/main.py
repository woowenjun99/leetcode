from collections import defaultdict
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        appeared = set(days)
        dp = defaultdict(int)
        for day in range(max(days) + 1):
            if day not in appeared: 
                dp[day] = dp[day - 1]
                continue
            dp[day] = min(costs[0] + dp[day - 1], costs[1] + dp[day - 7], costs[2] + dp[day - 30])
        return dp[days[-1]]
