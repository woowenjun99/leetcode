from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        answer = float("inf")
        for num in nums:
            new_num = 0
            while num > 0:
                new_num += num % 10
                num //= 10
            answer = min(answer, new_num)
        return answer