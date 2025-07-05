from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        answer = -1
        for key, value in counter.items():
            if key == value:
                answer = max(answer, value)
        return answer