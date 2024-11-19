from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        left = nums[0]
        for i in range(1, len(nums)):
            answer[i] = left
            left *= nums[i]
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer