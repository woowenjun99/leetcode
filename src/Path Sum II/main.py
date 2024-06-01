from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []

        def dfs(root, stack, currentSum):
            if not root: return
            if not root.left and not root.right and currentSum + root.val == targetSum:
                answer.append(stack.copy() + [root.val])
                return
            stack.append(root.val)
            dfs(root.left, stack, currentSum + root.val)
            dfs(root.right, stack, currentSum + root.val)
            stack.pop()
        
        dfs(root, [], 0)
        return answer