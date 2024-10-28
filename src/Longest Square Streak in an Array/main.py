from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        answer = -1
        for num in nums:
            if isinstance(num ** 0.5, int) in nums: continue
            count = 1
            while num ** 2 in nums:
                count += 1
                num = num ** 2
            if count == 1: continue
            answer = max(count, answer)
        return answer
