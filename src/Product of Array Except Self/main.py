from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        product = nums[0]
        for i in range(1, len(nums)):
            answer[i] = product
            product *= nums[i]

        product = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer