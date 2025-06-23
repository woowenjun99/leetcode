from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = [""]
        for i in range(len(s)):
            if len(answer[-1]) == k: answer.append("")
            answer[-1] += s[i]
        while len(answer[-1]) != k: answer[-1] += fill
        return answer
