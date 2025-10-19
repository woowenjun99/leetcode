from collections import deque
from typing import List

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        appeared: set[str] = set([s])
        queue: deque[str] = deque([s])
        answer = s
        while queue:
            current = queue.popleft()
            list_str = list(current)
            for i in range(1, len(list_str), 2): list_str[i] = str((int(list_str[i]) + a) % 10)
            joined = "".join(list_str)
            if joined not in appeared:
                appeared.add(joined)
                queue.append(joined)
                if joined < answer: answer = joined

            list_str: List[str] = []
            for i in range(len(current)): list_str.append(current[(i + b) % len(s)])
            joined = "".join(list_str)
            if joined not in appeared:
                appeared.add(joined)
                queue.append(joined)
                if joined < answer: answer = joined

        return answer