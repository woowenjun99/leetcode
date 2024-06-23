from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        answer = float("inf")
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            answer = min((nums[left] + nums[right]) / 2, answer)
            left += 1
            right -= 1
        return answer