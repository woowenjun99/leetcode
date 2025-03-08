from typing import List

class Solution:
    def __dfs(self, left: int, right: int, current: List[str], answer: List[str], n: int):
        if len(current) == 2 * n:
            answer.append("".join(current))
            return

        if right < left: self.__dfs(left, right + 1, current + [")"], answer, n)
        if left < n: self.__dfs(left + 1, right, current + ["("], answer, n)

    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        self.__dfs(1, 0, ["("], answer, n)
        return answer
