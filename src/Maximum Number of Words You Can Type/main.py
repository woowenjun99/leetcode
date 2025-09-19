class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        answer = 0
        for word in words:
            ans = 1
            for letter in brokenLetters:
                if letter in word:
                    ans = 0
            answer += ans
        return answer