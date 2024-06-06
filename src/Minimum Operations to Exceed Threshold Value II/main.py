from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        answer = 0
        while len(nums) >= 2 and nums[0] < k:
            answer += 1
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
        return answer