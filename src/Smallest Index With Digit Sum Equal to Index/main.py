from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            current = 0
            while num > 0:
                current += num % 10
                num //= 10
            if current == index: return index
        return -1