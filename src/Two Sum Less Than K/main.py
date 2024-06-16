from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = float("-inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < k:
                    answer = max(answer, nums[i] + nums[j])
        return -1 if answer == float("-inf") else answer