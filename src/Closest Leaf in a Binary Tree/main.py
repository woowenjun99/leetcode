from typing import Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.leaves = set()

    def dfs(self, node):
        if not node: return
        if node.left:
            self.dfs(node.left)
            self.graph[node.val].append(node.left.val)
            self.graph[node.left.val].append(node.val)
        if node.right:
            self.dfs(node.right)
            self.graph[node.val].append(node.right.val)
            self.graph[node.right.val].append(node.val)

        if not node.left and not node.right: self.leaves.add(node.val)

    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root)
        queue = deque([(k, 1)])
        visited = set()
        while queue:
            val, steps = queue.popleft()
            if val in self.leaves: return val
            for neighbour in self.graph[val]:
                if neighbour not in visited:
                    queue.append((neighbour, steps + 1))
                    visited.add(neighbour)