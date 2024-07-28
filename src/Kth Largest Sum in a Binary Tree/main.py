from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        responses = []
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if len(responses) != level: responses.append([])
            responses[level - 1].append(node.val)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))
        if len(responses) < k: return -1
        return sorted(map(lambda x: sum(x), responses), reverse=True)[k - 1]