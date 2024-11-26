from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = [[]]
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if len(levels) - 1 != level: levels.append([])
            levels[-1].append(node)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))
        
        for i in range(len(levels)):
            if i % 2 == 0: continue
            values = []
            for j in range(len(levels[i])): values.append(levels[i][j].val)
            for j in range(len(levels[i])): levels[i][j].val = values.pop()
        return root
