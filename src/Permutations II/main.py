from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        appeared = set()

        def backtracking(start):
            if start == len(nums):
                appeared.add(tuple(nums.copy()))
                return
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtracking(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        backtracking(0)
        return list(appeared)