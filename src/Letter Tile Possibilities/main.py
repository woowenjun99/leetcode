from typing import List

class Solution:
    def __init__(self):
        self.answer = set()

    def __backtracking(self, index: int, tiles: List[str], length: int, answer: List[str], used: List[bool]):
        if len(answer) == length:
            self.answer.add("".join(answer))
            return

        for i in range(len(tiles)):
            if used[i]: continue
            used[i] = True
            answer.append(tiles[i])
            self.__backtracking(index + 1, tiles, length, answer, used)
            answer.pop()
            used[i] = False

    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        used = [False] * len(tiles)
        for i in range(len(tiles)): self.__backtracking(0, tiles, i + 1, [], used)
        return len(self.answer)