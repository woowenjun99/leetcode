from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lca(self, root, p, q):
        if not root: return None
        if root.val == p or root.val == q: return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if left and right: return root
        if left: return left
        return right

    def bfs(self, start, dest):
        queue = deque([(start, 0)])
        while queue:
            front, steps = queue.popleft()
            if front.val == dest: return steps
            if front.left: queue.append((front.left, steps + 1))
            if front.right: queue.append((front.right, steps + 1))

    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        lca = self.lca(root, p, q)
        return self.bfs(lca, p) + self.bfs(lca, q)