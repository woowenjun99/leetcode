class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        stack = list(num)
        while stack and stack[-1] == "0": stack.pop()
        return "".join(stack)
