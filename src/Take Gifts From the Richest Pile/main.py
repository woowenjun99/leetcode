from heapq import heapify, heappop, heappush
from math import floor
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = list(map(lambda x: -x, gifts))
        heapify(gifts)
        for _ in range(k):
            gift = -heappop(gifts)
            heappush(gifts, -floor(gift ** 0.5))
        return -sum(gifts)
