from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cache = [0] * 60
        answer = 0
        for t in time:
            answer += cache[(60 - t % 60) % 60]
            cache[t % 60] += 1
        return answer