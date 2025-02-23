from typing import List, Optional

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        created = set()
        stack = [root]
        left = 1
        right = 0
        while left < len(preorder):
            if postorder[right] in created:
                stack.pop()
                right += 1
                continue
            node = TreeNode(preorder[left])
            created.add(preorder[left])
            left += 1
            if stack[-1].left is None: stack[-1].left = node
            else: stack[-1].right = node
            stack.append(node)
        return root