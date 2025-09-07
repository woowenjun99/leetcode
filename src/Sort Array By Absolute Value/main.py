from typing import List

class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        temp = sorted([(abs(num), num) for num in nums])
        return list(map(lambda x: x[1], temp))