from collections import deque

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for letter in s:
            if letter.lower() in {"a", "e", "i", "o", "u"}:
                vowels.append(letter)
        vowels = deque(sorted(vowels))
        s = list(s)
        for index in range(len(s)):
            if s[index].lower() in {"a", "e", "i", "o", "u"}:
                s[index] = vowels.popleft()
        return "".join(s)