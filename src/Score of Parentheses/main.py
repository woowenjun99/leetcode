class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == "(": 
                stack.append("(")
                continue
            if stack[-1] == "(":
                stack.pop()
                stack.append("1")
                continue
            current = 0
            while stack[-1] != "(":
                current += int(stack[-1])
                stack.pop()
            stack.pop()
            stack.append(str(2 * current))
        return sum(list(map(lambda x: int(x), stack)))