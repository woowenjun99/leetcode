from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                second = stack.pop()
                first = stack.pop()
                if token == "+": stack.append(first + second)
                if token == "-": stack.append(first - second)
                if token == "*": stack.append(first * second)
                if token == "/": stack.append(int(first / second))
            else: stack.append(int(token))
        return stack[0]