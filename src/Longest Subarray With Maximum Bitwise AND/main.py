from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        answer = counter = 0
        for i in range(len(nums)):
            if nums[i] != k:
                counter = 0
                continue
            counter += 1
            answer = max(counter, answer)
        return answer