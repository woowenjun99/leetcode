from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        responses = []
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if len(responses) != level: responses.append([])
            responses[level - 1].append(node.val)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

        for level in range(len(responses)):
            if level % 2 == 1:
                for num in responses[level]: 
                    if num % 2 == 1: return False
                for i in range(len(responses[level]) - 1):
                    if responses[level][i] <= responses[level][i + 1]: return False
            else:
                for num in responses[level]: 
                    if num % 2 == 0: return False
                for i in range(len(responses[level]) - 1):
                    if responses[level][i] >= responses[level][i + 1]: return False
        return True