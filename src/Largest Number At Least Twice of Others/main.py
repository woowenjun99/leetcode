from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_num = max(nums)
        for num in nums:
            if num == largest_num or largest_num >= 2 * num: continue
            return -1
        return nums.index(largest_num)