from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_words = Counter(words[0])
        for word in words:
            counter = Counter(word)
            for key in common_words:
                common_words[key] = min(common_words[key], counter[key])
        answer = []
        for key in common_words:
            for _ in range(common_words[key]): answer.append(key)
        return answer