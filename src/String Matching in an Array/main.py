from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = set()
        for i, candidate in enumerate(words):
            for j, word in enumerate(words):
                if i == j or candidate not in word: continue
                answer.add(candidate)
        return list(answer)