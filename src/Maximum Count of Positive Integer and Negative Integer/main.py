from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives = positives = 0
        for num in nums:
            if num < 0: negatives += 1
            elif num > 0: positives += 1
        return max(negatives, positives)
