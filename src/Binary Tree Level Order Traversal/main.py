from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        responses = []
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if len(responses) != level: responses.append([])
            responses[level - 1].append(node.val)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))
        return responses