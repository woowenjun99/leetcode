from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        start = 1
        for i in range(len(nums) - 1):
            if nums[i] == start:
                start += 1
                continue
            return False
        return nums[-1] == nums[-2] if len(nums) >= 2 else False
