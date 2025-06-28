from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        max_left = nums[0]
        answer = len(nums)
        for index in range(1, len(nums)):
            if nums[index] < max_left: answer -= 1
            else: max_left = max(max_left, nums[index])
        return answer