from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= len(nums): return len(nums)

        for i in range(len(nums)):
            x = len(nums) - i - 1
            if nums[i] < x and i + 1 < len(nums) and nums[i + 1] >= x: return x
        return -1
