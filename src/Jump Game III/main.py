from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = [False] * len(arr)
        visited[start] = True
        while queue:
            current = queue.popleft()
            if arr[current] == 0: return True
            if current - arr[current] >= 0 and not visited[current - arr[current]]:
                visited[current - arr[current]] = True
                queue.append(current - arr[current])
            if current + arr[current] < len(arr) and not visited[current + arr[current]]:
                visited[current + arr[current]] = True
                queue.append(current + arr[current])
        return False