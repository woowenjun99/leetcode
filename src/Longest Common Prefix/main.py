from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        for i in range(1, len(strs)):
            left = right = 0
            new_answer = []
            while left < len(answer) and right < len(strs[i]) and answer[left] == strs[i][right]:
                new_answer.append(answer[left])
                left += 1
                right += 1
            answer = "".join(new_answer)
        return answer
