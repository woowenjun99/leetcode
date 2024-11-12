from typing import List

class Solution:
    def __init__(self):
        self.stack = []
        self.answer = set()
        self.candidates = []
        self.target = 0

    def dfs(self, start: int, total: int):
        if total >= self.target:
            if total == self.target: self.answer.add(tuple(self.stack))
            return

        for index in range(start, len(self.candidates)):
            if index > start and self.candidates[index] == self.candidates[index - 1]: continue
            self.stack.append(self.candidates[index])
            self.dfs(index + 1, total + self.candidates[index])
            self.stack.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target
        self.dfs(0, 0)
        return list(self.answer)