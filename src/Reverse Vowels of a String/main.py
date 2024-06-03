from collections import deque

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for letter in s:
            if letter.lower() in {"a", "e", "i", "o", "u"}:
                vowels.append(letter)
        vowels = deque(vowels[::-1])
        s = list(s)
        for i in range(len(s)):
            if s[i].lower() in {"a", "e", "i", "o", "u"}:
                s[i] = vowels.popleft()
        return "".join(s)