from math import ceil
from typing import List

class Solution:
    def __hours_taken(self, piles: List[int], k: int):
        hour_taken = 0
        for pile in piles: hour_taken += ceil(pile / k)
        return hour_taken

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        answer = 0
        high = max(piles)
        while low <= high:
            k = low + (high - low) // 2
            if self.__hours_taken(piles, k) <= h:
                high = k - 1
                answer = k
            else: low = k + 1
        return answer
