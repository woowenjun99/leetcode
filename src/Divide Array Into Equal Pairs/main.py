from collections import Counter
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for value in counter.values():
            if value % 2 == 0: continue
            return False
        return True
