from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        answer = 1
        queue = deque([(root, 1)])
        while queue:
            node, streak = queue.popleft()
            answer = max(answer, streak)
            if node.left: queue.append((node.left, streak + 1 if node.val + 1 == node.left.val else 1))
            if node.right: queue.append((node.right, streak + 1 if node.val + 1 == node.right.val else 1))
        return answer