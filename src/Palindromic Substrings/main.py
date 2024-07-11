class Solution:
    def helper(self, left, right, s) -> str:
        answer = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            answer += 1
        return answer

    def countSubstrings(self, s: str) -> int:
        answer = len(s)
        for i in range(len(s)): answer += self.helper(i, i + 1, s) + self.helper(i - 1, i + 1, s)
        return answer