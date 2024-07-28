class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def dfs(self, root, p, q):
        if not root: return None
        if root.val == p.val or root.val == q.val: return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if left and right: return root
        return left if left else right
    
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = p
        while root.parent: root = root.parent
        return self.dfs(root, p, q)