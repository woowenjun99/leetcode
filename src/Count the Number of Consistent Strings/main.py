from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        answer = 0
        for word in words:
            idx = 0
            while idx < len(word):
                if word[idx] not in allowed: break
                idx += 1
            answer += 1 if idx == len(word) else 0
        return answer