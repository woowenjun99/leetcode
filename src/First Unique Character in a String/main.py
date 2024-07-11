from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mappers = Counter(s)
        for i in range(len(s)):
            if mappers[s[i]] == 1: return i
        return -1