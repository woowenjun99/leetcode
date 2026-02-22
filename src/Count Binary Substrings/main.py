class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        answer = 0
        stack = [[s[0], 1]]
        for i in range(1, len(s)):
            if s[i] == stack[-1][0]:
                stack[-1][1] += 1
                continue
            stack.append([s[i], 1])
        for i in range(len(stack) - 1): answer += min(stack[i][1], stack[i + 1][1])
        return answer