class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for letter in s:
            if stack and letter == ")" and stack[-1] == "(": 
                stack.pop()
                continue
            stack.append(letter)
        return len(stack)