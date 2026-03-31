class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        current_minimum = float("inf")
        index = -1
        for i, c in enumerate(capacity):
            if c >= itemSize and c < current_minimum:
                current_minimum = c
                index = i
        return index