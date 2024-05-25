from heapq import heappop, heappush

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq = []
        for num in nums:
            heappush(pq, num)
            if len(pq) > k: heappop(pq)
        return pq[0]