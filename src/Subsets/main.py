from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtracking(combinations, start, size):
            if len(combinations) == size: 
                answer.append(combinations.copy())
                return
            
            for index in range(start, len(nums)):
                combinations.append(nums[index])
                backtracking(combinations, index + 1, size)
                combinations.pop()

        for size in range(len(nums) + 1): backtracking([], 0, size)
        return answer