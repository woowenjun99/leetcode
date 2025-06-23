from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        answer = float("-inf")
        for i in range(len(nums) + 1): answer = max(abs(nums[i % len(nums)] - nums[(i + 1) % len(nums)]), answer)
        return answer