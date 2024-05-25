from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mappers = defaultdict(int)
        for i in range(len(s)): mappers[s[i]] += 1
        for i in range(len(s)):
            if mappers[s[i]] == 1: return i
        return -1