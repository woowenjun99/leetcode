from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index_reachable = 0
        for index, num in enumerate(nums):
            if max_index_reachable < index: return False
            max_index_reachable = max(index + num, max_index_reachable)
        return True
