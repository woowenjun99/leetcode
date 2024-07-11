from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = answer = 0
        mappers = defaultdict(int)
        for right in range(len(s)):
            mappers[s[right]] += 1
            while mappers[s[right]] > 1: 
                mappers[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer