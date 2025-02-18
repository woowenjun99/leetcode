from typing import List

class Solution:
    def __init__(self):
        self.answer = []

    def __backtracking(self, stack: List[str], pattern: str, used: set):
        if len(stack) == len(pattern) + 1:
            self.answer = stack
            return

        for i in range(1, 10):
            if i in used: continue
            if stack and pattern[len(stack) - 1] == "I" and i < int(stack[-1]): continue
            if stack and pattern[len(stack) - 1] == "D" and i > int(stack[-1]): continue
            used.add(i)
            self.__backtracking(stack + [str(i)], pattern, used)
            if self.answer: return
            used.remove(i)

    def smallestNumber(self, pattern: str) -> str:
        self.__backtracking([], pattern, set())
        return "".join(self.answer)