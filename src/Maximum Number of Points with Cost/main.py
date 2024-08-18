from typing import List
from collections import deque

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0]

        for idx in range(1, len(points)):
            ltr = [dp[0]]
            for col in range(1, len(points[idx])):
                ltr.append(max(ltr[-1] - 1, dp[col]))

            rtl = deque([dp[-1]])
            for col in range(len(points[idx]) - 2, -1, -1):
                rtl.appendleft(max(rtl[0] - 1, dp[col]))

            for col in range(len(points[idx])):
                dp[col] = points[idx][col] + max(ltr[col], rtl[col])

        return max(dp)