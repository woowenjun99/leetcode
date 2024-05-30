from collections import deque

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()             # Remove the leading whitespace
        if not s: return 0        # Handle empty string
        is_negative = s[0] == "-" # Check if it is a negative number
        start = 0
        if s[0] == "+" or s[0] == "-": start = 1
        stack = deque()
        while start < len(s) and s[start].isdigit():
            stack.append(int(s[start]))
            start += 1

        while stack and stack[0] == 0: stack.popleft()  # Handle many leading 0s
        if not stack: return 0                          # Handle empty stack

        answer = 0
        stack = list(stack)[::-1]
        while len(stack) > 1 and abs(answer) < 214748364:
            answer = answer * 10 + (stack[-1] if not is_negative else -stack[-1])
            stack.pop()

        if len(stack) > 1: return -2**31 if is_negative else 2**31 - 1 # Safeguard against big numbers

        if (not is_negative and answer > 214748364) or (is_negative and answer < -214748364):
            return -2**31 if is_negative else 2**31 - 1

        if abs(answer) == 214748364:
            if is_negative and stack[0] == 9: return -2**31
            elif not is_negative and stack[0] >= 8: return 2 ** 31 - 1

        return answer * 10 + (stack[-1] if not is_negative else -stack[-1])