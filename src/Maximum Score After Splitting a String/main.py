class Solution:
    def maxScore(self, s: str) -> int:
        answer = 0
        for i in range(1, len(s)):
            one_count = s[0:i].count("0")
            zero_count = s[i:].count("1")
            answer = max(answer, zero_count + one_count)
        return answer