from typing import List

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        new_heights = [0] * len(maximumHeight)
        new_heights[0] = maximumHeight[0]
        for index in range(1, len(maximumHeight)):
            if maximumHeight[index] >= new_heights[index - 1]:
                if new_heights[index - 1] - 1 <= 0: return -1
                new_heights[index] = new_heights[index - 1] - 1
                continue
            new_heights[index] = maximumHeight[index]
        return sum(new_heights)
