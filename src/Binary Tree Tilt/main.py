from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = 0

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.answer += abs(left - right)
        return root.val + left + right

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.answer