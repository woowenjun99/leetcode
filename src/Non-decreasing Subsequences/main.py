from typing import List

class Solution:
    def __init__(self):
        self.answer = set()

    def __backtracking(self, stack: List[int], length: int, start: int, nums: List[int]):
        if len(stack) == length:
            self.answer.add(tuple(stack))
            return
        if start == len(nums): return
        for i in range(start, len(nums)):
            if stack[-1] > nums[i]: continue
            stack.append(nums[i])
            self.__backtracking(stack, length, i + 1, nums)
            stack.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        for length in range(2, len(nums) + 1):
            for index, num in enumerate(nums):
                self.__backtracking([num], length, index + 1, nums)
        return list(self.answer)
