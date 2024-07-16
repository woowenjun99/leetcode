from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = list(map(set, words))
        answer = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]: answer += 1
        return answer