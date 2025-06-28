from math import prod
from typing import List

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        total = prod(nums)
        if total != target ** 2: return False

        answer = False
        def backtracking(index: int, stack: List[int], current_prod: int):
            nonlocal answer
            if current_prod == target:
                answer = True
                return
            if index == len(nums): return
            for i in range(index + 1, len(nums)):
                stack.append(nums[i])
                backtracking(i, stack, current_prod * nums[i])
                stack.pop()

        backtracking(0, [nums[0]], nums[0])
        return answer
