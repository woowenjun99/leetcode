from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = [""]
        current = 0
        for i in range(len(s)):
            if current < len(spaces) and i == spaces[current]:
                current += 1
                answer.append("")
            answer[-1] += s[i]
        return " ".join(answer)