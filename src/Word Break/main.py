from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) > len(s) or s[i:i+len(word)] != word: continue
                if not dp[i]: dp[i] = True and dp[i + len(word)]
        return dp[0]