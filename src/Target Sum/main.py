from functools import cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(current, index):
            if index == len(nums): return 1 if current == target else 0
            return dfs(current + nums[index], index + 1) + dfs(current - nums[index], index + 1)
        return dfs(0, 0)
