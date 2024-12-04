from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        stack = []
        for num in nums:
            if not stack or stack[-1] < num:
                stack.append(num)
                answer = max(answer, len(stack))
                continue
            stack = [num]

        stack = []
        for num in nums:
            if not stack or stack[-1] > num:
                stack.append(num)
                answer = max(answer, len(stack))
                continue
            stack = [num]
        return answer