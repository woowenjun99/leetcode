from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack or num != stack[-1]: stack.append(num)
        for i in range(len(stack)): nums[i] = stack[i]
        return len(stack)