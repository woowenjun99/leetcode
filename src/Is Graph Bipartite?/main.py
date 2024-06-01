from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        colours = [0] * v
        for i in range(v):
            if not colours[i]: # If we have not assigned this colour yet
                colours[i] = -1
                queue = deque([(i, -1)])
                while queue:
                    front, colour = queue.popleft()
                    for neighbour in graph[front]:
                        if not colours[neighbour]:
                            colours[neighbour] = -1 * colour
                            queue.append((neighbour, colours[neighbour]))
                            continue
                        if colours[neighbour] == colour: return False
        return True