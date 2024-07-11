from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for letter in ransomNote:
            if counter[letter] == 0: return False
            counter[letter] -= 1
        return True