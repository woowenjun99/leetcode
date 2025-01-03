from collections import defaultdict
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dp = defaultdict(int)
        vowels = {"a", "e", "i", "o", "u"}
        for i in range(len(words)):
            current = 1 if words[i][0] in vowels and words[i][-1] in vowels else 0
            dp[i] = current + dp[i - 1]

        answer = []
        for start, end in queries: answer.append(dp[end] - dp[start - 1])
        return answer
