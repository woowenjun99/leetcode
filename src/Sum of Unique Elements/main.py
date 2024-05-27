from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = 0
        for key in counter:
            if counter[key] != 1: continue
            total += key
        return total