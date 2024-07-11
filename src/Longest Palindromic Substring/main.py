from collections import deque

class Solution:
    def helper(self, left, right, s, dq) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            dq.appendleft(s[left])
            dq.append(s[right])
            left -= 1
            right += 1
        return "".join(dq)

    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            new_str_one = self.helper(i, i + 1, s, deque())
            new_str_two = self.helper(i - 1, i + 1, s, deque([s[i]]))
            if len(new_str_one) > len(answer): answer = new_str_one
            if len(new_str_two) > len(answer): answer = new_str_two
        return answer