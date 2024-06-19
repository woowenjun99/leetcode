from typing import List
from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        keys = counter.keys()
        answer = 0
        for key in keys:
            if key + 1 in counter: answer += counter[key]
        return answer