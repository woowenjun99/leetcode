from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_left = [0] * len(nums)
        for i in range(1, len(nums) - 1): max_left[i] = max(nums[i - 1], max_left[i - 1])
        max_right = [0] * len(nums)
        for i in range(len(nums) - 2, 0, -1): max_right[i] = max(nums[i + 1], max_right[i + 1])
        answer = 0
        for i in range(1, len(nums) - 1): answer = max(answer, (max_left[i] - nums[i]) * max_right[i])
        return answer