from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_of_array = sum(nums)
        total = 0
        for i in range(len(nums) + 1):
            total += i
        return total - sum_of_array