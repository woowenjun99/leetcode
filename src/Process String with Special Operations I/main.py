from typing import List

class Solution:
    def processStr(self, s: str) -> str:
        stack: List[str] = []
        for letter in s:
            if letter == "*":
                if stack: stack.pop()
                continue
            if letter == "#":
                stack += stack
                continue
            if letter == "%":
                stack = stack[::-1]
                continue
            stack.append(letter)
        return "".join(stack)