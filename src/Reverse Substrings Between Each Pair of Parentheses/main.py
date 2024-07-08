class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for letter in s:
            if letter == "(":
                stack.append([])
                continue
            elif letter == ")":
                letters = stack.pop()
                for i in range(len(letters) - 1, -1, -1): stack[-1].append(letters[i])
                continue
            stack[-1].append(letter)
        return "".join(stack[0])