from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        left = answer = 0
        right = len(warehouse) - 1
        boxes.sort(reverse=True)
        for box in boxes:
            if left <= right and box <= warehouse[left]:
                left += 1
                answer += 1
            elif right >= left and box <= warehouse[right]:
                right -= 1
                answer += 1
        return answer