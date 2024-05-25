from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        appeared = set()
        for word in words:
            if len(word) > 1 and word[:-1] not in appeared: continue
            appeared.add(word)
        longest_word = ""
        appeared = sorted(appeared)
        for word in appeared:
            if len(word) > len(longest_word): longest_word = word
        return longest_word