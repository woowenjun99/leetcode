from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dp = [0] * len(words)
        vowels = {"a", "e", "i", "o", "u"}
        dp[0] = 1 if words[0][0] in vowels and words[0][-1] in vowels else 0
        for i in range(1, len(words)):
            current = 1 if words[i][0] in vowels and words[i][-1] in vowels else 0
            dp[i] = current + dp[i - 1]

        answer = []
        for start, end in queries:
            if start == 0: answer.append(dp[end])
            else: answer.append(dp[end] - dp[start - 1])
        return answer