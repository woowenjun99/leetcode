class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            if not stack or stack[-1][0] != letter: 
                stack.append([letter, 1])
                continue
            if stack[-1][1] + 1 == k: 
                stack.pop()
                continue
            stack[-1][1] += 1
        answer = ""
        for letter, count in stack: answer += letter * count
        return answer
