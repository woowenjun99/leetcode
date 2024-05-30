from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = set()

        def backtracking(start, size, stack):
            if start == size:
                answers.add(tuple(sorted(stack)))
                return

            for i in range(start, len(nums)):
                stack.append(nums[i])
                backtracking(i + 1, size, stack)
                stack.pop()


        for size in range(len(nums) + 1): backtracking(0, size, [])

        return list(answers)