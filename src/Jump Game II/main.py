from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps_required = [float("inf")] * len(nums)
        jumps_required[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums): break
                jumps_required[i + j] = min(jumps_required[i + j], 1 + jumps_required[i])
        return jumps_required[-1]