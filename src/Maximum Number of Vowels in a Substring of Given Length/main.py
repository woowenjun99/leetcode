class Solution:
    def is_vowel(self, letter: str):
        return letter in {"a", "e", "i", "o", "u"}

    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for right in range(k):
            if not self.is_vowel(s[right]): continue
            count += 1

        answer = count
        right = k
        for right in range(k, len(s)):
            if self.is_vowel(s[right]): count += 1
            if self.is_vowel(s[right - k]): count -= 1
            answer = max(answer, count)
        
        return answer