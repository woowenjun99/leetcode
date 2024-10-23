from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        overall = []
        mappers = defaultdict(int)
        for i in range(1, len(nums) + 1): overall.extend(list(combinations(nums, i)))
        for all in overall:
            total = 0
            for num in all: total |= num
            mappers[total] += 1
        return mappers[max(mappers.keys())]