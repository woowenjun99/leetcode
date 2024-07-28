from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        paths = [str(root.val)]

        def dfs(node):
            if not node: return

            if node.left:
                paths.append(str(node.left.val))
                dfs(node.left)
                paths.pop()

            if node.right:
                paths.append(str(node.right.val))
                dfs(node.right)
                paths.pop()

            if not node.left and not node.right: answer.append("->".join(paths))

        dfs(root)
        return answer