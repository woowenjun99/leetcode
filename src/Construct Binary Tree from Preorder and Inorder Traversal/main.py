from typing import List, Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        created = set([preorder[0]])
        stack = [root]
        left, right = 1, 0
        while left < len(preorder):
            if inorder[right] in created:
                # Keep backtracking until we reach the node with value == inorder[right]
                while stack[-1].val != inorder[right]: stack.pop()

                # If inorder[right + 1] is not created yet, we know there is a right child so we create a new node on the right child
                if right + 1 < len(inorder) and inorder[right + 1] not in created:
                    stack[-1].right = TreeNode(preorder[left])
                    created.add(preorder[left])
                    left += 1
                    stack.append(stack[-1].right)
                right += 1
                continue
            created.add(preorder[left])
            node = TreeNode(preorder[left])
            stack[-1].left = node
            stack.append(node)
            left += 1
        return root
