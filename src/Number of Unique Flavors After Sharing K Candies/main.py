from collections import defaultdict
from typing import List

class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        outside = defaultdict(int)
        for i in range(k, len(candies)): outside[candies[i]] += 1
        answer = len(outside.keys())
        for i in range(len(candies) - k):
            answer = max(answer, len(outside.keys()))
            outside[candies[i]] += 1
            outside[candies[i + k]] -= 1
            if outside[candies[i + k]] == 0: del outside[candies[i + k]]
        return max(answer, len(outside.keys()))
    