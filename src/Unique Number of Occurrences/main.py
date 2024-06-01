from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        values = Counter(arr).values()
        return len(values) == len(set(values))