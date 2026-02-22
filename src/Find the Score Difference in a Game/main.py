from typing import List

class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        scores = [0, 0]
        active = 0
        for index, num in enumerate(nums):
            if num % 2 == 1: active = 1 - active
            if index != 0 and (index + 1) % 6 == 0: active = 1 - active
            scores[active] += num
        return scores[0] - scores[1]