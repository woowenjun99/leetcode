from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        value = 1
        answer = left = 0
        for right in range(len(nums)):
            value *= nums[right]
            while left <= right and value >= k:
                value //= nums[left]
                left += 1
            answer += (right - left) + 1
        return answer