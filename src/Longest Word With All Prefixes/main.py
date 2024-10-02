from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        set_of_words = set(words)
        answer = ""
        words.sort()
        for word in words:
            prefix = ""
            while len(prefix) < len(word):
                prefix += word[len(prefix)]
                if prefix not in set_of_words: break
            if word == prefix and len(word) > len(answer): answer = word
        return answer