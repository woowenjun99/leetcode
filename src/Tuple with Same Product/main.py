from collections import defaultdict
from math import perm
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): counter[nums[i] * nums[j]] += 1
        return 4 * sum([perm(value, 2) for value in counter.values()])