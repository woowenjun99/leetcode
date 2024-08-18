from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [-1] * len(arr)
        for i in range(len(arr) - 2, -1, -1): answer[i] = max(arr[i + 1], answer[i + 1])
        return answer