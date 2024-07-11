from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        answer = sorted([(-counter[word], word) for word in counter])
        return list(map(lambda x: x[1], answer[:k]))