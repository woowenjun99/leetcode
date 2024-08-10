from collections import Counter
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = set(map(lambda x: x[0], filter(lambda x: x[1] == 1, Counter(arr).items())))
        stack = []
        used = set()
        for element in arr:
            if element in counter and element not in used:
                stack.append(element)
                used.add(element)
        if k > len(stack): return ""
        return stack[k - 1]