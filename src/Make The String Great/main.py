class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for letter in s:
            if not stack or not (stack[-1] != letter and stack[-1].lower() == letter.lower()):
                stack.append(letter)
                continue
            stack.pop()
        return "".join(stack)