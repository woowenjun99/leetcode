from collections import deque

class Solution:
    def integerReplacement(self, n: int) -> int:
        queue = deque([(n, 0)])
        while queue:
            num, steps = queue.popleft()
            if num == 1: return steps
            if num % 2 == 0:
                queue.append((num // 2, steps + 1))
                continue
            queue.append((num + 1, steps + 1))
            queue.append((num - 1, steps + 1))