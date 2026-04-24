from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        answer = float("inf")
        for index, num in enumerate(nums):
            if num == target: answer = min(abs(index - start), answer)
        return answer