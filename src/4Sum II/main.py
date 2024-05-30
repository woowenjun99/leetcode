from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mappers = defaultdict(int)
        for k in nums3:
            for l in nums4: 
                mappers[l + k] += 1

        answer = 0
        for i in nums1:
            for j in nums2:
                if - i - j in mappers: answer += mappers[-i - j]

        return answer 