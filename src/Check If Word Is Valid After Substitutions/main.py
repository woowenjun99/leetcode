class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if len(stack) >= 2 and stack[-2] == "a" and stack[-1] == "b" and letter == "c":
                stack.pop()
                stack.pop()
                continue
            stack.append(letter)
        return len(stack) == 0