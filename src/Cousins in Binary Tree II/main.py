from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(1, root)])
        levels = deque([0])
        # Get the nodes at a certain level
        while queue:
            level, node = queue.popleft()
            if level != len(levels): levels.append(0)
            if node.left: 
                queue.append((level + 1, node.left))
                levels[-1] += node.left.val
            if node.right: 
                queue.append((level + 1, node.right))
                levels[-1] += node.right.val
        levels.appendleft(0)

        # Level order traversal again
        queue = deque([(0, root)])
        while queue:
            level, node = queue.popleft()
            if node == root: node.val = 0
            difference = levels[level + 1] - (node.left.val if node.left else 0) - (node.right.val if node.right else 0)
            if node.left:
                node.left.val = difference
                queue.append((level + 1, node.left))
            if node.right:
                node.right.val = difference
                queue.append((level + 1, node.right))
 
        return root