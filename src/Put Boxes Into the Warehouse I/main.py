from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        for i in range(1, len(warehouse)): warehouse[i] = min(warehouse[i - 1], warehouse[i])

        answer = 0
        for w in range(len(warehouse) - 1, -1, -1):
            if answer < len(boxes) and warehouse[w] >= boxes[answer]: answer += 1

        return answer