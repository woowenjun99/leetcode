from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = [[]]
        queue = deque([(root, 0, 1)])
        while queue:
            node, level, index = queue.popleft()
            if level + 1 != len(levels): levels.append([])
            levels[-1].append(index)
            if node.left is not None: queue.append((node.left, level + 1, 2 * index))
            if node.right is not None: queue.append((node.right, level + 1, 2 * index + 1))

        answer = 0
        for level in levels: answer = max(answer, level[-1] - level[0])
        return answer