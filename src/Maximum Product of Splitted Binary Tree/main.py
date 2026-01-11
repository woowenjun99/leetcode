from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums: List[int] = []

        def sum_of_subtree(node: Optional[TreeNode]):
            if node is None: return 0
            left = sum_of_subtree(node.left)
            subtree_sums.append(left)
            right = sum_of_subtree(node.right)
            subtree_sums.append(right)
            return node.val + left + right

        total = sum_of_subtree(root)
        answer = float("-inf")
        for subtree_sum in subtree_sums: answer = max(answer, subtree_sum * (total - subtree_sum))
        return answer % (10**9 + 7)