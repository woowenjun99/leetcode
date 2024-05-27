class Solution:
    def compressedString(self, word: str) -> str:
        answer, stack = [], []
        for letter in word:
            if stack and (len(stack) == 9 or stack[-1] != letter):
                answer.append(f"{len(stack)}{stack[-1]}")
                stack = []
            stack.append(letter)
        if stack: answer.append(f"{len(stack)}{stack[-1]}")
        return "".join(answer)