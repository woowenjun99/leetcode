from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(map(lambda x: x ** 2, nums))
        left = answer = 0
        right = len(nums) - 1
        while left <= right:
            answer += nums[right]
            right -= 1
            if left <= right:
                answer -= nums[left]
                left += 1
                continue
        return answer