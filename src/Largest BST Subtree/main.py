from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.val = val

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def postorder(node: Optional[TreeNode]):
            nonlocal answer
            if node is None: return True, 0, [float("inf"), float("-inf")]
            left = postorder(node.left)
            right = postorder(node.right)
            if not left[0] or not right[0]: return False, 0, [float("inf"), float("-inf")]
            if node.val <= left[2][1]: return False, 0, [float("inf"), float("-inf")]
            if node.val >= right[2][0]: return False, 0, [float("inf"), float("-inf")]
            answer = max(answer, 1 + left[1] + right[1])
            return True, 1 + left[1] + right[1], [min(node.val, left[2][0]), max(node.val, right[2][1])]

        postorder(root)
        return answer
