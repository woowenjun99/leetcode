from typing import List

class Solution:
    def min_days_required(self, weights: List[int], weight:int):
        current_weight = 0
        days_passed = 1
        for w in weights:
            if w > weight: return float("inf") # Cannot fit onto any ship
            if current_weight + w > weight:
                days_passed += 1
                current_weight = w
                continue
            current_weight += w
        return days_passed

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = min(weights)
        answer = 0
        high = sum(weights)
        while low <= high:
            mid = (high + low) // 2
            if self.min_days_required(weights, mid) <= days:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer