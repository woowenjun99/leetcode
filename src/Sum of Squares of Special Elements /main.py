from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for index, num in enumerate(nums):
            if n % (index + 1) == 0: answer += num ** 2
        return answer