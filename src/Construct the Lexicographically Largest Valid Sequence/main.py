from typing import List

class Solution:
    def __init__(self):
        self.answer = []

    def __backtracking(self, index: int, candidates: List[int], n: int, used: set):
        if index == (2 * n - 1):
            self.answer = candidates.copy()
            return

        if candidates[index] != 0:
            self.__backtracking(index + 1, candidates, n, used)
            return
        
        for i in range(n, 0, -1):
            if i in used or (i != 1 and index + i >= (2 * n - 1)) or (i != 1 and candidates[index + i] != 0): continue
            candidates[index] = i
            if i != 1: candidates[index + i] = i
            used.add(i)
            self.__backtracking(index + 1, candidates, n, used)
            if self.answer: return
            candidates[index] = 0
            if i != 1: candidates[index + i] = 0
            used.remove(i)

    def constructDistancedSequence(self, n: int) -> List[int]:
        for _ in range(n, -1, -1):
            candidates = [0] * (2 * n - 1)
            used = set()
            self.__backtracking(0, candidates, n, used)
            if self.answer: return self.answer
        return self.answer[0]