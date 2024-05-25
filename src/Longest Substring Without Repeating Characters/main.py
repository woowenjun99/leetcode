from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()
        response = 0
        dq = deque()
        for c in s:
            while used and c in used: used.remove(dq.popleft())
            dq.append(c)
            used.add(c)
            response = max(response, len(used))
        return response