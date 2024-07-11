from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float("-inf")
        total = 0
        for num in nums:
            total += num
            largest_sum = max(total, largest_sum)
            total = max(total, 0)
        return largest_sum