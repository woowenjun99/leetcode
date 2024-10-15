class Solution:
    def minimumSteps(self, s: str) -> int:
        answer = 0
        right = len(s) - 1
        for index in range(len(s) - 1, -1, -1):
            if s[index] == "0": continue
            answer += right - index
            right -= 1
        return answer