from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maximum_frequency = max(counter.values())
        return list(counter.values()).count(maximum_frequency) * maximum_frequency