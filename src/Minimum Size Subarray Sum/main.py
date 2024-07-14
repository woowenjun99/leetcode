from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = float("inf")
        left = total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                answer = min(answer, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if answer == float("inf") else answer