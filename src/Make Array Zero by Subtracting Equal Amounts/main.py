from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set([num for num in nums if num > 0])
        return len(s)
