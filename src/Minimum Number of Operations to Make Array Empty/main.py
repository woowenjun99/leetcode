from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        values = counter.values()
        if 1 in values: return -1
        total = 0
        for value in values:
            if value % 3 == 1:
                total += 2
                value -= 4
            if value % 3 == 2:
                total += 1
                value -= 2
            total += value // 3
        return total
