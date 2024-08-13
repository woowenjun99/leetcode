class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word[1:] == word[1:].lower()