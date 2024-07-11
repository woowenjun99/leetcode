from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = answer = 0
        right = len(height) - 1
        while left < right:
            answer = max((right - left) * min(height[left], height[right]), answer)
            if height[left] < height[right]: left += 1
            else: right -= 1
        return answer