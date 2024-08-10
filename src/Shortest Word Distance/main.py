from collections import deque
from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        queue = deque()
        visited = set()
        for index, word in enumerate(wordsDict):
            if word == word1: 
                queue.append((index, 0))
                visited.add(index)
        while queue:
            idx, steps = queue.popleft()
            if wordsDict[idx] == word2: return steps
            if idx - 1 >= 0 and idx - 1 not in visited:
                queue.append((idx - 1, steps + 1))
                visited.add(idx - 1)
            if idx + 1 < len(wordsDict) and idx + 1 not in visited:
                queue.append((idx + 1, steps + 1))
                visited.add(idx + 1)