from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        answer = left = count = 0
        for right in range(len(nums)):
            if nums[right] == 0: count += 1
            while count > k:
                if nums[left] == 0: count -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer