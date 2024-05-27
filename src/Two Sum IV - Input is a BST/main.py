from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        responses = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            responses.append(node.val)
            dfs(node.right)

        dfs(root)
        left, right = 0, len(responses) - 1
        while left < right:
            if responses[left] + responses[right] == k: return True
            if responses[left] + responses[right] < k: left += 1
            else: right -= 1
        return False