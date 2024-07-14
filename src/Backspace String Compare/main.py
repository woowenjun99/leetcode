class Solution:
    def helper(self, word):
        stack = []
        for letter in word:
            if letter == "#":
                if stack: stack.pop()
                continue
            stack.append(letter)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)