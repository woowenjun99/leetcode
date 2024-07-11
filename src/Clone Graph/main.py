from collections import defaultdict
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        adjacency_matrix = defaultdict(list)
        visited = set()

        def dfs(src):
            visited.add(src.val)
            for neighbor in src.neighbors:
                adjacency_matrix[src.val].append(neighbor.val)
                if neighbor.val in visited: continue
                dfs(neighbor)

        dfs(node)
        mappers = { key: Node(key) for key in visited } # Create a map for all the new nodes
        for key in adjacency_matrix:
            for child in adjacency_matrix[key]:
                mappers[key].neighbors.append(mappers[child])

        return mappers.get(node.val)