class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        consecutive_letters = set([("a", "z")])
        for i in range(25): consecutive_letters.add(tuple(sorted([chr(ord("a") + i), chr(ord("a") + i + 1)])))
        for letter in s:
            if stack and tuple(sorted([stack[-1], letter])) in consecutive_letters:
                stack.pop()
                continue
            stack.append(letter)
        return "".join(stack)