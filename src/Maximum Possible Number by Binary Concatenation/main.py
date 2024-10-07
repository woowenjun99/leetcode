from typing import List

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        nums = list(map(lambda num: bin(num)[2:], nums))
        solutions = sorted([
            int(nums[0] + nums[1] + nums[2], 2),
            int(nums[0] + nums[2] + nums[1], 2),
            int(nums[1] + nums[0] + nums[2], 2),
            int(nums[1] + nums[2] + nums[0], 2),
            int(nums[2] + nums[0] + nums[1], 2),
            int(nums[2] + nums[1] + nums[0], 2)
        ], reverse=True)
        return solutions[0]