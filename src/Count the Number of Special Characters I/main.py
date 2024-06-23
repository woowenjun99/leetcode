class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        answer = 0
        for i in range(26):
            letter = chr(ord("a") + i)
            if letter in s and letter.upper() in s: answer += 1
        return answer
        