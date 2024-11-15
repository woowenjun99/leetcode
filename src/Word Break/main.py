from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) > len(s) or s[i:i+len(word)] != word: continue
                dp[i] = True and dp[i+len(word)]
                if dp[i]: break
        return dp[0]