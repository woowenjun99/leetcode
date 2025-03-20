from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = answer = current = 0
        for right in range(len(nums)):
            while current & nums[right] != 0:
                current ^= nums[left]
                left += 1
            current |= nums[right]
            answer = max(answer, right - left + 1)
        return answer