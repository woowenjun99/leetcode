class Solution:
    def is_subsequence(self, proposed: str, original: str) -> bool:
        left = right = 0
        while left < len(proposed) and right < len(original):
            if proposed[left] == original[right]: left += 1
            right += 1
        return left == len(proposed)

    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t) - 1: return self.is_subsequence(s, t)
        if len(t) == len(s) - 1: return self.is_subsequence(t, s)
        if len(s) != len(t): return False
        count = 0
        for i in range(len(s)):
            if s[i] == t[i]: continue
            count += 1
        return count == 1