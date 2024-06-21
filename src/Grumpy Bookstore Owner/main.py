from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        covered_window = sum(customers[:minutes])
        uncovered_window = sum([customers[i] for i in range(minutes, len(customers)) if not grumpy[i]])
        maximum_satisfaction = uncovered_window + covered_window

        for i in range(len(customers) - minutes):
            if grumpy[i]: covered_window -= customers[i]
            if grumpy[minutes + i]: uncovered_window += customers[minutes + i]
            maximum_satisfaction = max(maximum_satisfaction, covered_window + uncovered_window)

        return maximum_satisfaction