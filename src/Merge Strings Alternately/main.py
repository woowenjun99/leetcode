class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = right = 0
        answer = []
        while left < len(word1) and right < len(word2):
            answer.append(word1[left])
            answer.append(word2[right])
            left += 1
            right += 1

        while left < len(word1):
            answer.append(word1[left])
            left += 1

        while right < len(word2):
            answer.append(word2[right])
            right += 1

        return "".join(answer)