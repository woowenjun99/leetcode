from typing import List

class Solution:
    def __can_match(self, candies: List[int], k: int, mid: int) -> bool:
        child = 0
        for candy in candies: child += candy // mid
        return child >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        answer = 0
        left = 1
        right = max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            if self.__can_match(candies, k, mid):
                answer = mid
                left = mid + 1
                continue
            right = mid - 1
        return answer