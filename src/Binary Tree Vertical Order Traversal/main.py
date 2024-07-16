from typing import List, Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        answer = []
        cache = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            cache[col].append(node.val)
            if node.left: queue.append((node.left, col - 1))
            if node.right: queue.append((node.right, col + 1))
        for key in sorted(cache.keys()): answer.append(cache[key])
        return answer