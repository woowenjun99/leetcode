from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(num, index) for index, num in enumerate(nums)]
        heapify(min_heap)
        for _ in range(k):
            num, index = heappop(min_heap)
            heappush(min_heap, (num * multiplier, index))
        for num, index in min_heap: nums[index] = num
        return nums
