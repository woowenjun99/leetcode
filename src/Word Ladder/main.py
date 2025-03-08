from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            word, step = queue.popleft()
            if word == endWord: return step
            w = list(word)
            for i in range(len(w)):
                temp = w[i]
                for j in range(26):
                    w[i] = chr(j + ord("a"))
                    if "".join(w) in visited or "".join(w) not in wordList: continue
                    visited.add("".join(w))
                    queue.append(("".join(w), step + 1))
                w[i] = temp
        return 0
