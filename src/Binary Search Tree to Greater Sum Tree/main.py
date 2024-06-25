class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        new_root = TreeNode(root.val)
        values = []

        def create_tree(root, new_root):
            if not root: return
            if root.left:
                new_root.left = TreeNode(root.left.val)
                create_tree(root.left, new_root.left)
            values.append(root.val)
            if root.right:
                new_root.right = TreeNode(root.right.val)
                create_tree(root.right, new_root.right)

        create_tree(root, new_root)
        for i in range(len(values) - 2, -1, -1): values[i] += values[i + 1]
        values = values[::-1]
        
        def dfs(root):
            if not root: return
            dfs(root.left)
            root.val = values.pop()
            dfs(root.right)

        dfs(new_root)
        return new_root