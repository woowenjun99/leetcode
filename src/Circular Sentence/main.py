class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for index in range(len(words) - 1):
            if words[index][-1] != words[index + 1][0]: return False
        return words[-1][-1] == words[0][0]