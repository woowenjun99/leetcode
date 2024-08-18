from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, root.val)])
        answer = 0
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                answer += val
                continue
            if node.left: queue.append((node.left, val * 10 + node.left.val))
            if node.right: queue.append((node.right, val * 10 + node.right.val))
        return answer