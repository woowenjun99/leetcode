from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque()
        appeared = set()
        longest_length = 0
        for char in s:
            while appeared and char in appeared: appeared.remove(dq.popleft())
            dq.append(char)
            longest_length = max(len(dq), longest_length)
        return longest_length
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))