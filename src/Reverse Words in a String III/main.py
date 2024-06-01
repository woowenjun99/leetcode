class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)): words[i] = "".join(list(words[i])[::-1])
        return " ".join(words)