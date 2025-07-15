from collections import Counter

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not word.isalnum(): return False
        counter = Counter(word.lower())
        vowel = counter["a"] + counter["e"] + counter["i"] + counter["o"] + counter["u"]
        if vowel == 0: return False
        has_consonant = False
        for i in range(26):
            if chr(ord("a") + i) not in {"a", "e", "i", "o", "u"} and chr(ord("a") + i) in counter:
                has_consonant = True
        return has_consonant
