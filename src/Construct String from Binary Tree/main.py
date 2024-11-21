from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        stack = [f"{root.val}"]

        def dfs(root):
            if not root: return None
            stack.append(f"({root.val}")
            dfs(root.left)
            if not root.left and root.right: stack.append("()")
            dfs(root.right)
            stack.append(")")

        dfs(root.left)
        if not root.left and root.right: stack.append("()")
        dfs(root.right)
        return "".join(stack)