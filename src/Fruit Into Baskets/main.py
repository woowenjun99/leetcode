from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter: defaultdict[int, int] = defaultdict(int)
        left = right = answer = 0
        while right < len(fruits):
            counter[fruits[right]] += 1
            while len(counter.keys()) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0: del counter[fruits[left]]
                left += 1
            answer = max(answer, sum(counter.values()))
            right += 1
        return answer
