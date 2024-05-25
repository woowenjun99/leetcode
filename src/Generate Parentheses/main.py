from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        response = []

        def dfs(left, right, value):
            if left == right == n:
                response.append("".join(value))
                return
            value.append("(")
            if left < n: dfs(left + 1, right, value)
            value.pop()
            value.append(")")
            if left > 0 and right != left: dfs(left, right + 1, value)
            value.pop()

        dfs(1, 0, ["("])
        return response