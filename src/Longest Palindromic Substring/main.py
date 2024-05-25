from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        def coroutine(left, right, dq: deque):
            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                dq.appendleft(s[left])
                dq.append(s[right])
                left -= 1
                right += 1
            if len(dq) > len(res): res = "".join(dq)
        
        for index in range(len(s)):
            coroutine(index - 1, index + 1, deque([s[index]]))
            coroutine(index, index + 1, deque())

        return res
