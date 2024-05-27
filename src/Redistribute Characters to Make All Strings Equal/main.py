from typing import List
from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = defaultdict(int)
        for word in words:
            for alphabet in word:
                counter[alphabet] += 1
        for value in counter.values():
            if value % len(words) != 0: return False
        return True