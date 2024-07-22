from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        responses = []
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if len(responses) != level: responses.append([])
            responses[level - 1].append(node.val)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

        minimum_level = 1
        minimum_value = sum(responses[0])
        for index, res in enumerate(responses):
            if sum(res) < minimum_value:
                minimum_level = index + 1
                minimum_value = sum(res)
        return minimum_level
