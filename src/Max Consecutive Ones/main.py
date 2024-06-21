from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = answer = 0
        for num in nums:
            if num == 0: count = 0
            else: count += 1
            answer = max(answer, count)
        return answer