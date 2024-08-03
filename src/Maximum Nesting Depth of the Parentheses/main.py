class Solution:
    def maxDepth(self, s: str) -> int:
        answer = count = 0
        for c in s:
            if c != "(" and c != ")": continue
            if c == ")": count -= 1
            else: count += 1
            answer = max(answer, count)
        return answer