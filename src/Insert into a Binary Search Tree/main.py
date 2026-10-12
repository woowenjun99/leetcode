class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None: return TreeNode(val)
        current = root
        previous = None
        while current:
            if current.val < val:
                previous = current
                current = current.right
            else:
                previous = current
                current = current.left
        if previous.val > val: previous.left = TreeNode(val)
        else: previous.right = TreeNode(val)
        return root