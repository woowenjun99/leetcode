from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = 0
        while counter < len(nums) and nums[counter] < k: counter += 1
        return counter