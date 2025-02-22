from typing import List

class Solution:
    def __init__(self):
        self.answer = []

    def __backtracking(self, stack: List[str], length: int, k: int):
        if len(stack) == length:
            self.answer.append("".join(stack))
            return

        letters = ["a", "b", "c"]
        for letter in letters:
            if not stack or stack[-1] != letter:
                self.__backtracking(stack + [letter], length, k)
                if len(self.answer) == k: return

    def getHappyString(self, n: int, k: int) -> str:
        self.__backtracking([], n, k)
        return self.answer[k - 1] if len(self.answer) >= k else ""