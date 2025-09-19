from collections import Counter
from typing import List

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return Counter(nums)[target] > len(nums) // 2
