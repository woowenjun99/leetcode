from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []
        for index, word in enumerate(words):
            if x not in word: continue
            answer.append(index)
        return answer