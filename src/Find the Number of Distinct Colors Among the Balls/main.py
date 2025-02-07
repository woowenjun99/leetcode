from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(int)
        total = 0
        answer = []
        counter = defaultdict(int)
        for index, colour in queries:
            counter[balls[index]] -= 1
            if counter[balls[index]] == 0: total -= 1
            balls[index] = colour
            counter[balls[index]] += 1
            if counter[balls[index]] == 1: total += 1
            answer.append(total)
        return answer