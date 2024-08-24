from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = []
        for index, num in enumerate(nums):
            if num != x: continue
            indices.append(index)
        return list(map(lambda q: indices[q - 1] if q <= len(indices) else -1, queries))