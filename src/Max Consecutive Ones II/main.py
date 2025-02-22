from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stack = []
        for index, num in enumerate(nums):
            if num == 0: continue
            if not stack or stack[-1][1] + 1 != index:
                stack.append([index, index])
                continue
            stack[-1][1] = index

        count = [0] * len(nums)
        for left, right in stack:
            start = left
            while start <= right:
                count[start] = right - left + 1
                start += 1

        answer = 0
        for i in range(len(nums)):
            if count[i] != 0:
                answer = max(count[i], answer)
                continue
            left = count[i - 1] if i - 1 >= 0 else 0
            right = count[i + 1] if i + 1 < len(nums) else 0
            answer = max(answer, 1 + left + right)
        return answer