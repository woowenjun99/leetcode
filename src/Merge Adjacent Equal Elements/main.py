from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
                continue
            current = num
            while stack and current == stack[-1]:
                stack.pop()
                current *= 2
            stack.append(current)
        return stack