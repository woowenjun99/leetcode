from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappers = {}
        for i in range(len(nums)):
            if nums[i] in mappers: return [mappers[nums[i]], i]
            mappers[target - nums[i]] = i