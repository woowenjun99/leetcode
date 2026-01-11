from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = [0]
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if level != len(levels) - 1: levels.append(0)
            levels[-1] += node.val
            if node.left is not None: queue.append((node.left, level + 1))
            if node.right is not None: queue.append((node.right, level + 1))
        
        max_so_far = levels[0]
        answer = 0
        for i in range(len(levels)):
            if levels[i] > max_so_far:
                answer = i
                max_so_far = levels[i]
        return answer + 1
