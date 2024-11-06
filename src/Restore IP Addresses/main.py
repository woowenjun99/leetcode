from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        stack = [s[0]]
        answer = []

        def backtracking(index: int = 1):
            if index == len(s):
                if len(stack) == 4:
                    answer.append(stack.copy())
                return
            temp = stack[-1]
            if 0 <= int(temp + s[index]) <= 255 and temp[0] != "0":
                stack[-1] += s[index]
                backtracking(index + 1)
                stack[-1] = temp
            stack.append(s[index])
            backtracking(index + 1)
            stack.pop()

        backtracking()
        return list(map(lambda word: ".".join(word), answer))
    