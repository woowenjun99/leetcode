from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        queue = deque([(root, chr(root.val + ord("a")))])
        candidates = []

        while queue:
            front, letters = queue.popleft()
            if not front.left and not front.right:
                candidates.append(letters)
                continue
            if front.left: queue.append((front.left, letters + chr(front.left.val + ord("a"))))
            if front.right: queue.append((front.right, letters + chr(front.right.val + ord("a"))))
        
        for index, letters in enumerate(candidates): candidates[index] = "".join(list(letters)[::-1])
        return sorted(candidates)[0]