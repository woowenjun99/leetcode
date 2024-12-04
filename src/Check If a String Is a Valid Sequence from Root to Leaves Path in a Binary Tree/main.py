from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        queue = deque([(root, 0)])
        while queue:
            node, index = queue.popleft()
            if index == len(arr) - 1:
                if not node.left and not node.right and node.val == arr[index]: return True
                continue
            if node.val != arr[index]: continue
            if node.left: queue.append((node.left, index + 1))
            if node.right: queue.append((node.right, index + 1))
        return False