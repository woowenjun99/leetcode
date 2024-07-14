from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        cache = {}

        def dfs(src):
            if src.val in cache: return cache[src.val]
            cloned = Node(src.val)
            cache[src.val] = cloned
            for neighbor in src.neighbors: cloned.neighbors.append(dfs(neighbor))
            return cloned

        return dfs(node)