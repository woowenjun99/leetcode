from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        answer = set(nums[0])
        for i in range(1, len(nums)): answer = answer.intersection(set(nums[i]))
        return sorted(answer)